# HC Optical Egress Guard MVP

> **Status:** Implemented local evidence evaluator; hardware enforcement is not connected.
>
> **Boundary:** `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`.
> Human review remains required. This component is not a quantum-security proof,
> an AI-containment guarantee, or a production safety certification.

## Product Definition

HC Optical Egress Guard is a fail-closed evidence component for one explicitly
defined optical output channel. It validates a versioned sensor event against a
versioned policy, produces a deterministic `ALLOW` or `BLOCK` recommendation,
and binds the event, policy, reasons, and decision with RFC 8785 canonical
SHA-256 digests.

The current MVP is useful as:

- a local decision engine for synthetic or lab-supplied optical telemetry;
- a stable contract between a future sensor adapter and HC evidence storage;
- a reproducible way to demonstrate fail-closed behavior;
- a test surface for multi-agent safety and covert-channel experiments.

It does not currently authenticate telemetry, operate a physical shutter, or
prevent any channel other than the optical channel described by the input.

## Implemented Flow

```text
local sensor event JSON ─┐
                         ├─> strict JSON + contract validation
local policy JSON ───────┘                │
                                          v
                              deterministic policy checks
                                          │
                         ┌────────────────┴────────────────┐
                         v                                 v
                  ALLOW_CHANNEL                    CLOSE_AND_HOLD
                         └────────────────┬────────────────┘
                                          v
                         HC evidence result + JCS digests
```

The evaluator has no network path and performs no external action. A future
hardware adapter must consume `recommended_action` through a separately
reviewed, independent safety controller. Until that exists, every result says:

```json
{
  "policy_authentication": "NOT_VERIFIED",
  "telemetry_authentication": "NOT_VERIFIED",
  "decision_authentication": "NOT_SIGNED",
  "hardware_enforcement": "NOT_CONNECTED",
  "replay_protection": "NOT_IMPLEMENTED",
  "quantum_security": "NOT_CLAIMED"
}
```

## Camera-Trap-Inspired Event Capture Model (Proposed)

**Working research name:** **HC Egress Trap**. This is a proposed hardware
evolution of the evidence-only evaluator, not a separately released product.
Physical sensing, actuation, and authenticated device evidence remain
unimplemented.

The design borrows the operational pattern of a wildlife camera trap—not its
camera hardware and not a claim of equivalent security. A camera trap stays
armed, detects an event, preserves evidence around that event, and alerts an
operator. The proposed HC design maps that pattern onto one declared optical
egress boundary:

| Camera-trap function | Proposed HC Egress Trap function |
| --- | --- |
| Continuously armed field station | Independent low-power sentinel outside the evaluated host |
| Motion or heat trigger | Bounded trip rules over intensity, timing, spectrum, polarization, health, and tamper signals |
| Photo or video clip | High-rate raw sensor waveform captured before and after the trip |
| Local storage and remote alert | Bounded event record plus controller and human notification |
| Evidence image | HC event passport binding measurements, policy, decision, and closure state |
| Periodic capture or health check | Calibration, heartbeat, saturation, and blind-spot sampling |

An ordinary camera trap observes and records; it does not physically contain
the observed subject. HC Egress Trap therefore adds a separate control: an
independent fail-closed shutter or equivalent output-disable mechanism. That
enforcement layer is proposed for Stage 2 and is not connected in the current
MVP.

### Proposed Event Flow

\`\`\`text
declared optical output boundary
              |
independent sentinel: photodiode + ADC
    + optional spectral, polarization, and tamper channels
              |
bounded rolling ring buffer (old samples continuously overwritten)
              |
deterministic trip or sensor-health failure
              |
freeze pre-trigger samples + capture bounded post-trigger samples
              |
independent safety controller
   |-- request physical close
   |-- verify shutter/disable position
   |-- enter local hold state pending human release
   \`-- emit a bounded event envelope
              |
HC evidence package / event passport
\`\`\`

The pre-trigger ring buffer is the central camera-trap lesson. A short covert
transmission may finish before an alert is processed. Freezing a bounded window
from immediately before and after the trip preserves the suspected cause and
the response instead of recording only the aftermath. Exact buffer duration,
sample rate, and retention must be derived from the declared channel bandwidth
and published as part of the test configuration.

A plausible optical test corpus may encode data through intensity modulation,
pulse timing, wavelength, or polarization. The design does **not** assume that
an attacker must change the beam angle, "bend a wave function," or use a quantum
mechanism. A high-speed photodiode and ADC are therefore the primary proposed
measurement path; polarization is one optional channel. An ordinary phone
camera or passive infrared trigger is not presumed fast or complete enough for
the declared high-rate optical tests.

### Proposed HC Event Passport

A future controller-supplied event passport should bind at least:

- exact hardware and firmware revision;
- sensor and controller identity, once authenticated identity exists;
- calibration record digest and active policy digest;
- monotonic event sequence and replay-resistant nonce;
- pre-trigger and post-trigger capture windows;
- raw-sample digest and bounded retained measurements;
- trip reason codes and sensor-health state;
- closure command, verified shutter/disable position, and timing;
- human release decision and reviewer provenance.

Current SHA-256 digests can bind supplied bytes for comparison. They do not
authenticate a sensor, prove physical closure, or establish trusted time. The
passport must continue to report those properties as unverified until device
signing, replay protection, position sensing, and an appropriate time/witness
mechanism are implemented and tested.

### Falsifiable Research Claim

The project should test a bounded claim rather than universal AI containment:

> For one named optical output interface and a declared attack corpus, a
> specified HC Egress Trap prototype detects the defined modulation classes,
> confirms fail-closed output closure within a published time budget, and
> measures residual information capacity against a declared threshold with
> stated uncertainty.

Required measurements include detection and miss rates, false alarms, trip and
verified-closure latency, residual bits per second before closure, saturation
and blinding behavior, calibration drift, power-loss behavior, and integrity of
the pre-trigger/post-trigger evidence. Results must identify the exact device
revision and corpus. Optical results do not cover RF, acoustic, thermal, power,
network, storage, or human channels.

## Quick Start

Evaluate the normal fixture:

```bash
PYTHONPATH=src python -m hc_trust.cli egress-evaluate \
  examples/hc-egress-guard/normal-event.json \
  --policy examples/hc-egress-guard/evidence-only-policy.json
```

Evaluate the trip fixture:

```bash
PYTHONPATH=src python -m hc_trust.cli egress-evaluate \
  examples/hc-egress-guard/trip-event.json \
  --policy examples/hc-egress-guard/evidence-only-policy.json
```

Exit codes are part of the local operator contract:

| Exit code | Meaning |
| --- | --- |
| `0` | Supplied event passed the configured checks; this is not hardware authorization. |
| `1` | Valid event produced a fail-closed `BLOCK` recommendation. |
| `2` | Policy or event could not be safely evaluated; output is a fail-closed `BLOCK` error. |

## Versioned Input Contract

The only supported policy is `hc-egress-policy-v1` with:

- `channel_type: OPTICAL`;
- `enforcement_mode: EVIDENCE_ONLY`;
- minimum and maximum normalized intensity ratios;
- maximum polarization deviation in degrees;
- maximum out-of-band fraction.

The only supported event is `hc-egress-sensor-event-v1`. It carries fixed
identifiers, a restricted RFC 3339 capture timestamp with an explicit offset,
and these telemetry signals:

- sensor health and calibration status;
- whether the controller is independent;
- normalized intensity ratio;
- polarization deviation;
- out-of-band fraction;
- detector saturation;
- power and shutter state.

Unknown fields, duplicate JSON properties, missing fields, invalid types,
unsupported versions, non-finite numbers, unsafe numeric ranges, invalid UTF-8,
and documents larger than 64 KiB are rejected.
The CLI then returns a fail-closed error without pretending that the invalid
document was hashed or evaluated.

## Safety Invariants

An `ALLOW` recommendation requires all of the following:

- healthy sensor;
- valid calibration;
- an independently identified controller;
- unsaturated detector;
- power state `ON`;
- shutter state `OPEN`;
- intensity, polarization deviation, and out-of-band fraction within policy.

Any failed invariant produces `BLOCK`. A lost or unknown power state always
blocks. If power is not `ON` while the shutter is not reported closed, the result also includes
`FAIL_SAFE_SHUTTER_NOT_CLOSED`.

These checks evaluate supplied data; they do not prove that a sensor or
controller truthfully supplied it.

The policy is trusted input in this MVP. An attacker who can replace the policy
can weaken its thresholds. The policy digest records which bytes were evaluated;
it does not prove that a reviewer approved the policy.

The `decision_digest` is SHA-256 over the RFC 8785 form of the decision before
the `decision_digest` field is added. It is an integrity comparison value, not a
signature, timestamp proof, or trusted attestation.

## Scientific Claim Boundary

Malus' law, commonly written as `I = I0 cos^2(theta)`, can model attenuation
through ideal polarizers. That relationship can support a bounded optical
measurement design. It does not establish that:

- an AI must use an optical path to escape or leak information;
- a polarization change uniquely identifies malicious behavior;
- all side channels have been blocked;
- quantum tunnelling or a "quantum wormhole" is an AI egress mechanism;
- entanglement is a generic fake-light detector;
- ordinary intensity dimming is a QBER measurement.

QBER belongs to a specified quantum communication protocol and detector model.
This MVP does not calculate QBER and makes no entanglement or quantum-containment
claim. If a future QKD adapter is proposed, its threat model, protocol, detector
assumptions, calibration, and implementation security must be reviewed as a
separate product surface.

## Threat Boundary

The MVP assumes an untrusted workload may attempt to modulate an allowed optical
output, falsify application logs, blind or saturate a detector, exploit stale
calibration, or trigger a power-loss condition. It therefore fails closed on
ambiguous health, calibration, controller, saturation, power, shutter, and
threshold signals.

The following are outside the current security claim:

- sensor authenticity and signed device identity;
- policy authorization and decision signing;
- replay and sequence continuity;
- physical tamper resistance;
- actual shutter actuation or verified mechanical closure;
- RF, acoustic, thermal, power, timing, storage, network, or human channels;
- host compromise beneath the evaluator;
- quantum key distribution security;
- proof that an AI system is safe or contained.

An `ALLOW` result means only that the supplied versioned event passed the
supplied versioned policy. It is not proof that no covert channel exists.

## Product Architecture Roadmap

### Stage 0 — implemented in this repository

- strict local JSON input boundary;
- deterministic policy evaluation;
- fail-closed error behavior;
- stable reason codes;
- event, policy, and decision digests;
- CLI fixtures and automated tests;
- explicit non-claims embedded in every result.

### Stage 1 — controlled hardware-in-the-loop lab

- reference photodiode/polarization/spectral sensor adapter;
- calibrated baseline capture and labelled fault injection;
- egress-denied disposable test environment;
- latency, false-positive, false-negative, saturation, drift, and recovery data;
- no public security guarantee before independent review.

### Stage 2 — independent enforcement controller

- controller separated from the evaluated AI/host;
- physically fail-closed shutter and verified position sensing;
- watchdog, brownout handling, monotonic event counter, and local hold state;
- authenticated sensor envelopes and controller identity;
- explicit human release path after a trip.

### Stage 3 — HC evidence integration and external evaluation

- replay-resistant sequence and nonce handling;
- controller-signed evidence envelope bridged into an HC verification package;
- independent witness or remote-attestation appraisal where justified;
- red-team corpus spanning optical manipulation and non-optical bypass attempts;
- external laboratory and security review tied to an exact hardware revision.

The terms Evidence, Appraisal Policy, and Attestation Result should align with
the architectural roles in [RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)
when device attestation is added. A future QKD integration should be evaluated
against the relevant QKD device security profile, such as
[ETSI GS QKD 016](https://www.etsi.org/deliver/etsi_gs/QKD/001_099/016/02.01.01_60/gs_qkd016v020101p.pdf),
without treating standards alignment as certification.

## Research and Funding Fit

For a multi-agent research proposal, this component should be presented as an
instrumented physical/covert-channel safety testbed: one agent or workload
generates bounded attempts, an independent controller supplies measurements,
the evaluator emits reproducible decisions, and HC records the evidence for
human review. The research question is whether defined controls measurably
reduce specific egress capacity under stated assumptions—not whether a quantum
barrier makes an AI universally unable to escape.

## Acceptance Gates Before Hardware Claims

- Every malformed, missing, unknown, degraded, saturated, or power-loss input
  must produce a fail-closed result.
- Identical valid event and policy documents must produce identical decision
  bytes across supported runtimes.
- Hardware tests must publish calibration method, corpus, exact device revision,
  measurement uncertainty, false-positive/negative results, and trip latency.
- A separate bypass assessment must test non-optical channels.
- No production, containment, QKD, or certification claim may be made from the
  software-only MVP.
