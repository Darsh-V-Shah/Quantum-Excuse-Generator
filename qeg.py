# ============================================================
# Q.E.G. — QUANTUM EXCUSE GENERATOR
# Crazy App Contest Edition
# ============================================================

import gradio as gr
import random
import math
import html
from datetime import datetime


# ============================================================
# GLOBAL STATE
# ============================================================

STATE = {
    "case_id": None,
    "level": 1,
    "mode": "Schrödinger",
    "situation": "",
    "universe": None,
    "lore": [],
    "entities": [],
    "last_excuse": "",
    "history": [],
    "collapsed": False
}


# ============================================================
# QUANTUM MODES
# ============================================================

MODES = {

    "Schrödinger": {
        "icon": "☢",
        "description": "The excuse exists in multiple states until observed.",
        "effect": "Superposition"
    },

    "Heisenberg": {
        "icon": "Δ",
        "description": "The more we know about the excuse, the less certain it becomes.",
        "effect": "Uncertainty"
    },

    "Many Worlds": {
        "icon": "∞",
        "description": "Every possible excuse occurs in a parallel universe.",
        "effect": "Timeline Divergence"
    },

    "Entanglement": {
        "icon": "⛓",
        "description": "Your excuse becomes quantumly linked to another event.",
        "effect": "Non-local Causality"
    },

    "Quantum Tunneling": {
        "icon": "⇝",
        "description": "The excuse bypasses obstacles that should make it impossible.",
        "effect": "Barrier Penetration"
    },

    "Thermodynamic": {
        "icon": "ΔS",
        "description": "The universe becomes increasingly unable to explain what happened.",
        "effect": "Entropy"
    },

    "Black Hole": {
        "icon": "●",
        "description": "The excuse becomes so dense that information cannot escape.",
        "effect": "Information Collapse"
    },

    "ABSOLUTELY UNHINGED": {
        "icon": "☠",
        "description": "The laws of physics have been formally revoked.",
        "effect": "Reality Failure"
    }
}


# ============================================================
# QUANTUM TERMINOLOGY
# ============================================================

QUANTUM_TERMS = [
    "quantum superposition",
    "wave-function collapse",
    "decoherence",
    "probability amplitude",
    "quantum tunneling",
    "observer effect",
    "quantum entanglement",
    "temporal interference",
    "causal inversion",
    "spontaneous symmetry breaking",
    "vacuum fluctuation",
    "many-worlds branching",
    "quantum uncertainty",
    "dimensional instability",
    "chronological displacement",
    "non-local causality",
    "entropy cascade",
    "information collapse",
    "timeline decoherence",
    "probabilistic causality"
]


# ============================================================
# UNIVERSAL ENTANGLEMENT OBJECTS
# ============================================================

ENTANGLEMENT_OBJECTS = [
    "the Wi-Fi router",
    "the attendance server",
    "the university timetable",
    "the professor's coffee",
    "the classroom projector",
    "the assignment portal",
    "the campus network",
    "the department printer",
    "the college clock",
    "the laboratory computer",
    "the canteen samosa",
    "the university timeline",
    "the academic calendar",
    "the dean's email inbox"
]


# ============================================================
# PROFESSOR REACTIONS
# ============================================================

PROFESSOR_REACTIONS = [
    "Professor hostility increased by 17%.",
    "Professor hostility remains in superposition.",
    "The professor has become causally entangled with the excuse.",
    "The professor's skepticism has crossed the classical threshold.",
    "The professor has requested experimental evidence.",
    "The professor is now observing the system.",
    "The professor has entered the quantum reference frame.",
    "The professor's patience has undergone spontaneous symmetry breaking.",
    "The professor has been detected in an alternate timeline."
]


# ============================================================
# KEYWORD DETECTION
# ============================================================

KEYWORD_ENTITIES = {

    "assignment": [
        "assignment",
        "homework",
        "project",
        "submission",
        "submit",
        "report"
    ],

    "attendance": [
        "attendance",
        "present",
        "absent",
        "presence"
    ],

    "professor": [
        "professor",
        "teacher",
        "sir",
        "ma'am",
        "madam",
        "faculty"
    ],

    "oversleep": [
        "overslept",
        "oversleep",
        "sleep",
        "woke",
        "alarm",
        "late"
    ],

    "exam": [
        "exam",
        "test",
        "quiz",
        "midterm",
        "final"
    ],

    "class": [
        "class",
        "lecture",
        "lesson"
    ],

    "wifi": [
        "wifi",
        "wi-fi",
        "internet",
        "network",
        "connection"
    ],

    "deadline": [
        "deadline",
        "due",
        "due date",
        "last date"
    ]
}


# ============================================================
# STARTING EXCUSES
# ============================================================

STARTERS = {

    "assignment":
        "I was unable to submit the assignment because the deadline entered a state of temporal uncertainty.",

    "attendance":
        "I was physically present, but my attendance existed in a separate probability state.",

    "professor":
        "I attempted to contact the professor, but the communication channel experienced quantum decoherence.",

    "oversleep":
        "I overslept because my consciousness failed to collapse into the waking state.",

    "exam":
        "I was prepared for the exam, but my knowledge distribution collapsed into an unfavorable state.",

    "class":
        "I missed the class because my location became uncertain relative to the classroom.",

    "wifi":
        "The Wi-Fi connection underwent spontaneous quantum decoherence at the exact moment I needed it.",

    "deadline":
        "The deadline became temporally ambiguous and briefly existed in multiple possible positions.",

    "default":
        "The situation resulted from an unexpected interaction between human activity and quantum probability."
}


# ============================================================
# ESCALATION COMPONENTS
# ============================================================

ESCALATION_POOL = [

    "The event was amplified by a localized probability fluctuation.",

    "This caused the relevant wave function to partially decohere.",

    "A secondary timeline briefly became causally dominant.",

    "The resulting quantum state could not be measured without altering it.",

    "An observer effect prevented accurate reconstruction of the incident.",

    "The university network became entangled with the event.",

    "A temporal feedback loop was detected approximately 4.7 milliseconds later.",

    "The original cause was subsequently observed to have caused itself.",

    "Multiple versions of the event began interfering with one another.",

    "The distinction between cause and consequence became statistically insignificant.",

    "The academic timeline experienced measurable curvature.",

    "A nearby probability branch appears to have absorbed the missing information.",

    "Reality briefly violated its own conservation laws.",

    "The event produced a non-zero probability of having never happened.",

    "The system has exceeded the recommended level of scientific nonsense.",

    "The university timeline has lost causal integrity.",

    "The professor is now an emergent phenomenon.",

    "Attendance has spontaneously broken its own symmetry.",

    "The original timeline has been classified as experimental data.",

    "Further investigation may cause additional universes."
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def generate_case_id():

    timestamp = datetime.now().strftime("%H%M%S")

    random_part = random.randint(100, 999)

    return f"QEG-{timestamp}-{random_part}"


def detect_entities(situation):

    text = situation.lower()

    found = []

    for entity, keywords in KEYWORD_ENTITIES.items():

        for keyword in keywords:

            if keyword in text:
                found.append(entity)
                break

    return found


def choose_starter(entities):

    for entity in entities:

        if entity in STARTERS:
            return STARTERS[entity]

    return STARTERS["default"]


def random_quantum_term():

    return random.choice(QUANTUM_TERMS)


def random_entanglement():

    return random.choice(ENTANGLEMENT_OBJECTS)


def random_professor_reaction():

    return random.choice(PROFESSOR_REACTIONS)


# ============================================================
# TELEMETRY
# ============================================================

def generate_telemetry(mode, level):

    object_name = random_entanglement()

    telemetry = [

        "INITIALIZING QUANTUM EXCUSE ENGINE",

        "Loading probability matrix...",

        "Generating probability amplitudes...",

        "Establishing excuse superposition...",

        f"Quantum mode selected: {mode}",

        "Scanning alternate timelines...",

        "Measuring plausible deniability...",

        "Calculating professor hostility...",

        f"Entangling excuse with {object_name}...",

        "Searching for causally convenient universes...",

        "Normalizing probability distribution...",

        "Detecting observer effect...",

        f"Escalation level: {level}",

        "Preparing wave-function collapse..."
    ]

    return telemetry


# ============================================================
# EXCUSE GENERATOR
# ============================================================

def generate_excuse(situation, mode, level):

    situation = situation.strip()

    if not situation:
        situation = "something went wrong"

    entities = detect_entities(situation)

    starter = choose_starter(entities)

    situation_clean = html.escape(situation)

    mode_data = MODES[mode]

    excuse = starter

    # --------------------------------------------------------
    # MODE-SPECIFIC GENERATION
    # --------------------------------------------------------

    if mode == "Schrödinger":

        excuse = (
            f"{starter} "
            f"The event simultaneously existed in both the successful "
            f"and unsuccessful state until observed. "
            f"Observation unfortunately collapsed the system into the "
            f"less convenient outcome."
        )

    elif mode == "Heisenberg":

        excuse = (
            f"{starter} "
            f"According to the uncertainty relationship governing the incident, "
            f"precisely determining what happened would make it impossible "
            f"to determine when it happened."
        )

    elif mode == "Many Worlds":

        excuse = (
            f"{starter} "
            f"In at least one parallel universe, the task was completed correctly. "
            f"Unfortunately, our branch of reality appears to have inherited "
            f"the outcome from a less successful timeline."
        )

    elif mode == "Entanglement":

        entangled = random_entanglement()

        excuse = (
            f"{starter} "
            f"The event became quantumly entangled with {entangled}. "
            f"As a result, changes in one system produced non-local effects "
            f"in the other."
        )

    elif mode == "Quantum Tunneling":

        excuse = (
            f"{starter} "
            f"The system attempted to tunnel through the practical barriers "
            f"preventing completion. The tunneling probability was technically "
            f"non-zero, but unfortunately so was the probability of failure."
        )

    elif mode == "Thermodynamic":

        excuse = (
            f"{starter} "
            f"Entropy increased throughout the process until the original "
            f"sequence of events became thermodynamically irreversible."
        )

    elif mode == "Black Hole":

        excuse = (
            f"{starter} "
            f"The information associated with the incident collapsed beyond "
            f"the event horizon of a localized academic black hole. "
            f"No classical explanation can currently escape."
        )

    elif mode == "ABSOLUTELY UNHINGED":

        excuse = (
            f"{starter} "
            f"The event subsequently triggered a vacuum fluctuation, "
            f"three unauthorized timeline branches, and an administrative "
            f"singularity. At this stage, conventional causality is no longer "
            f"a supported feature."
        )

    # --------------------------------------------------------
    # ESCALATION
    # --------------------------------------------------------

    if level >= 2:

        excuse += " " + random.choice(ESCALATION_POOL)

    if level >= 3:

        excuse += " " + random.choice(ESCALATION_POOL)

    if level >= 4:

        excuse += " " + random.choice(ESCALATION_POOL)

    if level >= 5:

        excuse += (
            " The resulting system has exceeded normal academic "
            "causal boundaries."
        )

    if level >= 6:

        excuse += (
            " Further observation may produce additional realities."
        )

    if level >= 7:

        excuse += (
            " At this point, submitting an explanation may itself "
            "alter the timeline."
        )

    if level >= 8:

        excuse += (
            " The universe has officially stopped cooperating."
        )

    if level >= 9:

        excuse += (
            " The original event is now classified as a "
            "quantum administrative anomaly."
        )

    if level >= 10:

        excuse += (
            " Please do not attempt to reproduce this experiment "
            "without appropriate academic supervision."
        )

    return excuse


# ============================================================
# METRICS
# ============================================================

def calculate_metrics(level, mode):

    base = random.Random(level * 137 + len(mode))

    coherence = max(
        5,
        min(99, 95 - level * 3 + base.randint(-4, 4))
    )

    scientific_confidence = max(
        20,
        min(99, 58 + level * 4 + base.randint(-5, 5))
    )

    believability = max(
        1,
        min(99, 82 - level * 7 + base.randint(-5, 5))
    )

    hostility = max(
        1,
        min(99, 15 + level * 8 + base.randint(-4, 4))
    )

    unhingedness = max(
        1,
        min(100, level * 10 + base.randint(-3, 3))
    )

    return {
        "Quantum Coherence": coherence,
        "Scientific Confidence": scientific_confidence,
        "Believability": believability,
        "Professor Hostility": hostility,
        "Unhingedness": unhingedness
    }


# ============================================================
# METRIC BAR
# ============================================================

def metric_bar(name, value):

    safe_name = html.escape(name)

    return f"""
    <div class="metric-row">

        <div class="metric-header">

            <span>{safe_name}</span>

            <span>{value}%</span>

        </div>

        <div class="metric-track">

            <div class="metric-fill"
                 style="width:{value}%">
            </div>

        </div>

    </div>
    """


# ============================================================
# RESULT HTML
# ============================================================

def build_result_html(excuse, metrics, mode, level, case_id):

    metric_html = ""

    for name, value in metrics.items():

        metric_html += metric_bar(name, value)

    return f"""

    <div class="result-panel">

        <div class="result-top">

            <div>

                <div class="small-label">
                    EXCUSE STATE
                </div>

                <div class="collapse-status">
                    COLLAPSED
                </div>

            </div>

            <div class="case-id">
                CASE ID<br>
                <b>{case_id}</b>
            </div>

        </div>


        <div class="excuse-box">

            <div class="small-label">
                QUANTUM EXCUSE
            </div>

            <div class="excuse-text">
                {html.escape(excuse)}
            </div>

        </div>


        <div class="explanation-box">

            <div class="small-label">
                QUANTUM INTERPRETATION
            </div>

            <p>
                The excuse was generated using
                <b>{html.escape(mode)}</b>
                mechanics at escalation level
                <b>{level}</b>.
            </p>

            <p>
                The system introduced probabilistic causality,
                observer effects and timeline instability to explain
                the reported event.
            </p>

        </div>


        <div class="metrics-box">

            <div class="small-label">
                SYSTEM METRICS
            </div>

            {metric_html}

        </div>


        <div class="footer-data">

            UNIVERSE: {random.randint(100000,999999)}
            &nbsp;&nbsp;|&nbsp;&nbsp;
            MODE: {html.escape(mode)}
            &nbsp;&nbsp;|&nbsp;&nbsp;
            LEVEL: {level}

        </div>

    </div>
    """


# ============================================================
# LORE GENERATOR
# ============================================================

def generate_lore(level):

    lore = [

        "Wi-Fi router experienced anomalous quantum fluctuations.",

        "Attendance server became entangled with the university network.",

        "Temporal feedback loop detected.",

        "University timeline experienced causal instability.",

        "Professor entered an alternate observation frame.",

        "Academic reality has exceeded safe operating parameters."
    ]

    if level <= 2:
        return lore[:2]

    if level <= 4:
        return lore[:3]

    if level <= 6:
        return lore[:4]

    if level <= 8:
        return lore[:5]

    return lore


# ============================================================
# COLLAPSE WAVE FUNCTION
# ============================================================

def collapse_wavefunction(situation, mode, reality, confidence, style):

    if not situation.strip():

        return (
            "⚠ SYSTEM ERROR: No situation supplied.",
            "<div class='error-box'>Enter a mundane problem before collapsing the wave function.</div>",
            ""
        )

    # Reset case
    STATE["case_id"] = generate_case_id()
    STATE["level"] = 1
    STATE["mode"] = mode
    STATE["situation"] = situation
    STATE["collapsed"] = True

    # Universe
    STATE["universe"] = random.randint(
        100000,
        999999
    )

    STATE["entities"] = detect_entities(situation)

    # Generate
    excuse = generate_excuse(
        situation,
        mode,
        STATE["level"]
    )

    STATE["last_excuse"] = excuse

    STATE["history"] = [excuse]

    STATE["lore"] = generate_lore(
        STATE["level"]
    )

    metrics = calculate_metrics(
        STATE["level"],
        mode
    )

    # Telemetry
    telemetry = generate_telemetry(
        mode,
        STATE["level"]
    )

    telemetry_html = ""

    for line in telemetry:

        telemetry_html += (
            f"<div class='telemetry-line'>"
            f"> {html.escape(line)}"
            f"</div>"
        )

    # Result
    result_html = build_result_html(
        excuse,
        metrics,
        mode,
        STATE["level"],
        STATE["case_id"]
    )

    # Lore
    lore_html = ""

    for item in STATE["lore"]:

        lore_html += (
            f"<div class='lore-line'>"
            f"◆ {html.escape(item)}"
            f"</div>"
        )

    return (
        excuse,
        result_html,
        telemetry_html + lore_html
    )


# ============================================================
# MAKE IT MORE QUANTUM
# ============================================================

def make_more_quantum():

    if not STATE["collapsed"]:

        return (
            "⚠ Collapse the wave function first.",
            "",
            ""
        )

    STATE["level"] += 1

    if STATE["level"] > 10:

        STATE["level"] = 10

    mode = STATE["mode"]

    excuse = generate_excuse(
        STATE["situation"],
        mode,
        STATE["level"]
    )

    STATE["last_excuse"] = excuse

    STATE["history"].append(
        excuse
    )

    STATE["lore"] = generate_lore(
        STATE["level"]
    )

    metrics = calculate_metrics(
        STATE["level"],
        mode
    )

    result_html = build_result_html(
        excuse,
        metrics,
        mode,
        STATE["level"],
        STATE["case_id"]
    )

    lore_html = ""

    for item in STATE["lore"]:

        lore_html += (
            f"<div class='lore-line'>"
            f"◆ {html.escape(item)}"
            f"</div>"
        )

    status = (
        f"QUANTUM ESCALATION LEVEL {STATE['level']}/10"
    )

    return (
        excuse,
        result_html,
        f"<div class='escalation-status'>{status}</div>"
        + lore_html
    )


# ============================================================
# RANDOM SCENARIO
# ============================================================

RANDOM_SCENARIOS = [

    "Why didn't I submit my assignment?",

    "Why was I absent from class?",

    "Why didn't I reply to the professor?",

    "Why did I miss the exam?",

    "Why wasn't my attendance recorded?",

    "Why did my Wi-Fi stop working before the deadline?",

    "Why did I arrive late to class?",

    "Why did the assignment disappear from my laptop?",

    "Why did I forget about the deadline?",

    "Why was I unable to attend the morning lecture?"

]


def random_scenario():

    return random.choice(
        RANDOM_SCENARIOS
    )


# ============================================================
# RESET
# ============================================================

def reset_all():

    STATE["case_id"] = None
    STATE["level"] = 1
    STATE["mode"] = "Schrödinger"
    STATE["situation"] = ""
    STATE["universe"] = None
    STATE["lore"] = []
    STATE["entities"] = []
    STATE["last_excuse"] = ""
    STATE["history"] = []
    STATE["collapsed"] = False

    return (
        "",
        "",
        "",
        50,
        80,
        "Deadpan Scientific"
    )


# ============================================================
# EXPORT REPORT
# ============================================================

def generate_report():

    if not STATE["collapsed"]:

        return "No quantum excuse has been collapsed yet."

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
============================================================
Q.E.G. — QUANTUM EXCUSE REPORT
============================================================

CASE ID:
{STATE["case_id"]}

TIMESTAMP:
{timestamp}

MODE:
{STATE["mode"]}

ESCALATION LEVEL:
{STATE["level"]}/10

UNIVERSE:
{STATE["universe"]}

------------------------------------------------------------
ORIGINAL SITUATION
------------------------------------------------------------

{STATE["situation"]}

------------------------------------------------------------
FINAL QUANTUM EXCUSE
------------------------------------------------------------

{STATE["last_excuse"]}

------------------------------------------------------------
QUANTUM LORE
------------------------------------------------------------

"""

    for item in STATE["lore"]:

        report += f"◆ {item}\n"

    report += """
------------------------------------------------------------
SYSTEM STATUS
------------------------------------------------------------

EXCUSE STATE: COLLAPSED
CAUSALITY: UNSTABLE
REALITY: QUESTIONABLE
PROFESSOR HOSTILITY: UNKNOWN

============================================================
GENERATED BY Q.E.G.
Quantum Excuse Generator
============================================================
"""

    return report


# ============================================================
# CUSTOM CSS
# ============================================================

CSS = """

body {

    background:
        radial-gradient(
            circle at top,
            #101a2b 0%,
            #05070b 45%,
            #020306 100%
        );

}


.gradio-container {

    max-width: 1400px !important;

    background:
        radial-gradient(
            circle at top,
            #101a2b 0%,
            #05070b 55%,
            #020306 100%
        ) !important;

    color: #e8faff !important;

    font-family:
        "Courier New",
        monospace !important;

}


.title {

    text-align: center;

    font-size: 54px;

    font-weight: 900;

    letter-spacing: 8px;

    color: #ffffff;

    text-shadow:
        0 0 10px #00eaff,
        0 0 25px #00eaff;

    margin-bottom: 0;

}


.subtitle {

    text-align: center;

    color: #7defff;

    font-size: 16px;

    letter-spacing: 3px;

    margin-bottom: 30px;

}


.lab-card {

    background:
        rgba(4, 10, 18, 0.88);

    border:
        1px solid rgba(0, 234, 255, 0.25);

    border-radius: 12px;

    padding: 20px;

    box-shadow:
        0 0 25px rgba(0, 234, 255, 0.06);

}


.small-label {

    color: #61eaff;

    font-size: 11px;

    letter-spacing: 3px;

    margin-bottom: 8px;

}


.excuse-box {

    background:
        rgba(0, 234, 255, 0.025);

    border-left:
        3px solid #00eaff;

    padding: 20px;

    margin-top: 20px;

}


.excuse-text {

    font-size: 20px;

    line-height: 1.7;

    color: #ffffff;

}


.collapse-status {

    font-size: 26px;

    font-weight: bold;

    color: #70ffcf;

    text-shadow:
        0 0 10px #70ffcf;

}


.case-id {

    text-align: right;

    font-size: 11px;

    color: #788899;

}


.explanation-box {

    margin-top: 20px;

    padding: 18px;

    border:
        1px solid rgba(150, 100, 255, 0.25);

    background:
        rgba(120, 70, 255, 0.035);

}


.metrics-box {

    margin-top: 20px;

    padding: 18px;

}


.metric-row {

    margin-bottom: 15px;

}


.metric-header {

    display: flex;

    justify-content: space-between;

    color: #b8d9e5;

    font-size: 12px;

    margin-bottom: 5px;

}


.metric-track {

    width: 100%;

    height: 5px;

    background: #101a22;

    border-radius: 10px;

    overflow: hidden;

}


.metric-fill {

    height: 100%;

    background:
        linear-gradient(
            90deg,
            #00eaff,
            #8d6cff
        );

    box-shadow:
        0 0 10px #00eaff;

}


.footer-data {

    margin-top: 20px;

    padding-top: 12px;

    border-top:
        1px solid rgba(255,255,255,0.08);

    font-size: 10px;

    color: #53636e;

}


.telemetry-line {

    color: #62dfff;

    font-size: 12px;

    margin-bottom: 7px;

}


.lore-line {

    color: #927cff;

    font-size: 12px;

    margin-top: 8px;

}


.escalation-status {

    color: #ff61d8;

    font-weight: bold;

    margin-bottom: 15px;

    text-shadow:
        0 0 8px #ff61d8;

}


.error-box {

    color: #ff6b7a;

    border:
        1px solid #ff4458;

    padding: 15px;

    background:
        rgba(255, 40, 70, 0.05);

}


button {

    font-family:
        "Courier New",
        monospace !important;

}


#collapse-button {

    background:
        linear-gradient(
            90deg,
            #00a9c4,
            #754cff
        ) !important;

    color: white !important;

    font-weight: bold !important;

    border: none !important;

    box-shadow:
        0 0 20px rgba(0, 234, 255, 0.25);

}


#quantum-button {

    background:
        linear-gradient(
            90deg,
            #5b22ff,
            #d126a9
        ) !important;

    color: white !important;

    font-weight: bold !important;

    border: none !important;

}


textarea,
input {

    background: #050a10 !important;

    color: #dffaff !important;

    border:
        1px solid rgba(0, 234, 255, 0.2) !important;

}


label {

    color: #a7d8e5 !important;

}


"""



# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(
    title="Q.E.G. — Quantum Excuse Generator",
    css=CSS,
    theme=gr.themes.Base()
) as app:

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    gr.HTML(
        """
        <div class="title">
            Q.E.G.
        </div>

        <div class="subtitle">
            QUANTUM EXCUSE GENERATOR
            &nbsp; // &nbsp;
            CLASSICAL EXCUSES ARE PREDICTABLE
        </div>
        """
    )


    # --------------------------------------------------------
    # MAIN INPUT
    # --------------------------------------------------------

    with gr.Row():

        with gr.Column(
            scale=5,
            elem_classes=["lab-card"]
        ):

            gr.Markdown(
                "## ⚛ DEFINE THE INCIDENT"
            )

            situation = gr.Textbox(
                label="What happened?",
                placeholder=(
                    "Example: Why didn't I submit my assignment?"
                ),
                lines=4
            )


            random_button = gr.Button(
                "🎲 GENERATE RANDOM INCIDENT"
            )


            gr.Markdown(
                "## ⚛ QUANTUM PARAMETERS"
            )


            mode = gr.Dropdown(
                choices=list(MODES.keys()),
                value="Schrödinger",
                label="Quantum Mode"
            )


            reality = gr.Slider(
                minimum=0,
                maximum=100,
                value=50,
                step=1,
                label="Reality Distortion"
            )


            confidence = gr.Slider(
                minimum=0,
                maximum=100,
                value=80,
                step=1,
                label="Scientific Confidence"
            )


            style = gr.Dropdown(
                choices=[
                    "Deadpan Scientific",
                    "Corporate",
                    "Extremely Serious",
                    "Academic",
                    "Completely Unhinged"
                ],
                value="Deadpan Scientific",
                label="Delivery Style"
            )


            collapse_button = gr.Button(
                "⚛ COLLAPSE WAVE FUNCTION",
                elem_id="collapse-button",
                size="lg"
            )


            quantum_button = gr.Button(
                "☢ MAKE IT MORE QUANTUM",
                elem_id="quantum-button",
                size="lg"
            )


        # ----------------------------------------------------
        # TELEMETRY
        # ----------------------------------------------------

        with gr.Column(
            scale=4,
            elem_classes=["lab-card"]
        ):

            gr.Markdown(
                "## ◈ QUANTUM TELEMETRY"
            )

            telemetry = gr.HTML(
                value="""
                <div class="telemetry-line">
                > SYSTEM STANDBY
                </div>

                <div class="telemetry-line">
                > Awaiting incident...
                </div>

                <div class="telemetry-line">
                > Quantum engine ready.
                </div>
                """
            )


    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    gr.Markdown(
        "## ◈ COLLAPSED RESULT"
    )


    result = gr.HTML(
        value="""
        <div class="lab-card">

            <div class="small-label">
                SYSTEM STATUS
            </div>

            <div style="
                color:#667784;
                font-size:14px;
                padding:30px 0;
            ">

                No wave function has been collapsed.

                <br><br>

                Enter a mundane problem above.

                <br>

                The universe is waiting.

            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # ACTIONS
    # --------------------------------------------------------

    with gr.Row():

        reset_button = gr.Button(
            "↻ RESET EXPERIMENT"
        )

        report_button = gr.Button(
            "▣ GENERATE QUANTUM REPORT"
        )


    report = gr.Textbox(
        label="Quantum Excuse Report",
        lines=15,
        interactive=False
    )


    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    collapse_button.click(

        fn=collapse_wavefunction,

        inputs=[
            situation,
            mode,
            reality,
            confidence,
            style
        ],

        outputs=[
            situation,
            result,
            telemetry
        ]

    )


    quantum_button.click(

        fn=make_more_quantum,

        inputs=[],

        outputs=[
            situation,
            result,
            telemetry
        ]

    )


    random_button.click(

        fn=random_scenario,

        inputs=[],

        outputs=[
            situation
        ]

    )


    reset_button.click(

        fn=reset_all,

        inputs=[],

        outputs=[
            situation,
            result,
            telemetry,
            reality,
            confidence,
            style
        ]

    )


    report_button.click(

        fn=generate_report,

        inputs=[],

        outputs=[
            report
        ]

    )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 65)
    print("        Q.E.G. — QUANTUM EXCUSE GENERATOR")
    print("=" * 65)
    print()
    print("Quantum Excuse Engine: ONLINE")
    print("Reality Distortion System: ONLINE")
    print("Timeline Scanner: ONLINE")
    print("Professor Hostility Monitor: ONLINE")
    print()
    print("Opening local interface...")
    print()
    print("URL: http://127.0.0.1:7860")
    print()
    print("Keep this terminal running while using Q.E.G.")
    print("=" * 65)
    print()

    app.launch(

        server_name="127.0.0.1",

        server_port=7860,

        share=False,

        debug=False,

        inbrowser=True

    )
