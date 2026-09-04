from pathlib import Path

# Trigger revision: journal-targeted preparation workflow.
ROOT = Path(__file__).resolve().parents[1]
tex_path = ROOT / 'CP20_MANUSCRIPT.tex'
tex = tex_path.read_text(encoding='utf-8')

marker = r'\date{}'
metadata = r'''\date{}
\subjclass[2020]{Primary 11B83; Secondary 37B10, 37B40, 68R15}
\keywords{Syracuse map, Collatz problem, valuation words, factor complexity, Sturmian words, thermodynamic pressure}
'''
if r'\subjclass[2020]' not in tex:
    if marker not in tex:
        raise SystemExit('date marker not found')
    tex = tex.replace(marker, metadata, 1)

old_disclosure = r'''\section*{Disclosure and funding}

\paragraph{AI-assisted research disclosure.}
AI systems were used during the broader research programme for conjecture exploration, symbolic and numerical experimentation, proof-audit preparation, literature screening, and drafting assistance.  The mathematical claims included here were selected from the project's audited/frozen result set, and the author assumes responsibility for the manuscript, its citations, and its final claims.  This paragraph should be adapted to the policy of the eventual journal before submission.

\paragraph{Funding.}
This work received no external funding.
'''
replacement = r'''\section*{Funding}
This work received no external funding.

\section*{Declaration of competing interest}
The author declares no competing interests.
'''
if old_disclosure in tex:
    tex = tex.replace(old_disclosure, replacement, 1)
elif 'This paragraph should be adapted to the policy of the eventual journal before submission.' in tex:
    raise SystemExit('Disclosure block changed unexpectedly')

repro_marker = r'''For the critical-density numerics, the canonical certificate source is
\path{CP20_TASK8A_RIGOROUS_CERTIFICATE_V3.py}, with its frozen saved output and manifest hashes.  The finite-\(B\) and infinite-envelope constants are likewise supported by the frozen pressure-generalization certificate package.  A final submission package should list the exact source paths and hashes alongside the manuscript.
'''
ai_research = repro_marker + r'''
\subsection*{Research workflow and use of AI-assisted tools}\label{sec:ai-workflow}
AI-assisted research tools, including OpenAI ChatGPT, OpenAI Codex, and Anthropic Claude, were used in the broader research workflow for conjecture exploration, symbolic-derivation checks, computational-script drafting, literature screening, and adversarial proof-audit preparation.  Outputs from these tools were treated as untrusted candidate material rather than as authority.  Claims selected for this paper were retained only after separate exact derivations, reproducible computational certificates where applicable, and dedicated zero-trust audit passes.  The AI tools are not authors.  The author selected the research direction and claims, reviewed the final manuscript and citations, and takes full responsibility for the mathematical statements and conclusions.
'''
if 'Research workflow and use of AI-assisted tools' not in tex:
    if repro_marker not in tex:
        raise SystemExit('Reproducibility marker not found')
    tex = tex.replace(repro_marker, ai_research, 1)

bib_marker = r'''\bibliographystyle{amsplain}
\bibliography{CP20_REFERENCES}
'''
declaration = r'''\section*{Declaration of generative AI and AI-assisted technologies in the manuscript preparation process}
During the preparation of this work, the author used OpenAI ChatGPT, OpenAI Codex, and Anthropic Claude to assist with content organization, language editing, literature screening, and preparation of reproducibility materials.  AI-assisted tools were also used in the research workflow as described above.  After using these tools, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication.

''' + bib_marker
if 'Declaration of generative AI and AI-assisted technologies in the manuscript preparation process' not in tex:
    if bib_marker not in tex:
        raise SystemExit('Bibliography marker not found')
    tex = tex.replace(bib_marker, declaration, 1)

tex_path.write_text(tex, encoding='utf-8')

outdir = ROOT / 'submission_jnt'
outdir.mkdir(parents=True, exist_ok=True)

cover = """Dear Editors of the Journal of Number Theory,

Please consider the manuscript “Factor-Complexity and Pressure Barriers for Critical-Log Syracuse Valuation Words” by Halil Talha Ertan for publication in the Journal of Number Theory.

The paper studies a conditional structural regime for positive odd-only Syracuse orbits. Under the global critical-log law s_k = kappa log_2 k + O(1), it proves an exponential lower bound for valuation-word factor complexity. It then combines this arithmetic lower bound with deterministic constrained-word pressure estimates to obtain finite-alphabet and uniform zero-critical obstructions, including the certified threshold kappa > 2.784, and a two-type critical-site density pressure inequality.

The manuscript does not claim to prove the Collatz conjecture and does not exclude divergent or cyclic behavior in general. The novelty claim is deliberately restricted to the quantitative Syracuse-specific rate/pressure/density chain. Close prior work on repeated-factor divisibility, Sturmian codings, entropy barriers, and thermodynamic formalism is discussed explicitly.

The manuscript contains a detailed disclosure of AI-assisted research and manuscript-preparation tools in accordance with Elsevier's current policy. AI-assisted outputs were treated as untrusted candidate material and the final claims were subjected to separate adversarial audits and reproducible checks where applicable. I take full responsibility for the manuscript and all of its mathematical statements, citations, and conclusions.

For clarity, a separate manuscript by the author concerning polynomial collision energy for the Syracuse random variable is currently under review elsewhere. The present submission concerns factor complexity and deterministic pressure under a critical-log orbit hypothesis; its principal theorem set is distinct and the present manuscript is not under consideration by any other journal.

The manuscript is 17 pages in the current amsart format. Suggested 2020 MSC classifications are 11B83 (primary), 37B10, 37B40, and 68R15 (secondary).

Thank you for your consideration.

Sincerely,
Halil Talha Ertan
Independent Researcher, Turkey
haliltalhaertan@gmail.com
"""
(outdir / 'CP20_JNT_COVER_LETTER.txt').write_text(cover, encoding='utf-8')

highlights = """Critical-log Syracuse orbits force exponential valuation-word complexity.
Finite-alphabet zero-critical words satisfy a deterministic pressure bound.
A uniform pressure envelope yields the certified threshold kappa > 2.784.
Critical-site densities obey an explicit two-type pressure inequality.
The results are conditional and do not prove the Collatz conjecture.
"""
(outdir / 'CP20_JNT_HIGHLIGHTS.txt').write_text(highlights, encoding='utf-8')

checklist = """# CP20 Journal of Number Theory submission package

Target journal: Journal of Number Theory (Elsevier)

## Submission metadata
- Title: Factor-Complexity and Pressure Barriers for Critical-Log Syracuse Valuation Words
- Author: Halil Talha Ertan
- Affiliation: Independent Researcher, Turkey
- Email: haliltalhaertan@gmail.com
- Primary MSC: 11B83
- Secondary MSC: 37B10, 37B40, 68R15
- Keywords: Syracuse map; Collatz problem; valuation words; factor complexity; Sturmian words; thermodynamic pressure
- Funding: none
- Competing interests: none declared

## Policy notes
- The manuscript explicitly states that it does not prove the Collatz conjecture.
- A journal-specific AI declaration is included immediately before the references.
- A separate research-workflow disclosure explains AI-assisted theorem exploration, code drafting, literature screening, and audit preparation.
- The author retains full responsibility for the paper.
- The same manuscript is not under consideration elsewhere.

## Files
- CP20_MANUSCRIPT.tex
- CP20_REFERENCES.bib
- submission_jnt/CP20_JNT_COVER_LETTER.txt
- submission_jnt/CP20_JNT_HIGHLIGHTS.txt
- submission_jnt/CP20_MANUSCRIPT_JNT.pdf

## Final portal checks
- Confirm article type: Research Paper / Full Length Article (or nearest current JNT option).
- Copy title, abstract, keywords, MSC codes, author/affiliation exactly.
- Upload the compiled PDF.
- Upload source files if the portal requests them at initial submission.
- Paste the AI declaration exactly as stated in the manuscript if the portal asks separately.
- State that there is no duplicate or simultaneous submission of this manuscript.
- Do not characterize the paper as a proof of Collatz.
"""
(outdir / 'CP20_JNT_SUBMISSION_CHECKLIST.md').write_text(checklist, encoding='utf-8')
