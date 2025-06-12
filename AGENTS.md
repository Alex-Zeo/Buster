# AGENTS.md – Buster

*Spec for OpenAI Codex & human contributors*

## 1  Overview

### Purpose
Buster is a Discord bot that collects user messages and linked content to automatically compile and submit sanction violation reports to the Office of Foreign Assets Control (OFAC).

### Design Goals
- Automate data collection from Discord conversations
- Validate user-provided links and extract relevant evidence
- Generate consistent OFAC reports and file them automatically
- Provide clear logging and audit trails

### Execution Environment
- Python 3.11 or newer
- Discord API credentials
- Internet access to submit reports

#### Buster Agent Service Goals
1. Accurately gather all reportable content from chat
2. Ensure reports meet OFAC formatting and compliance rules
3. Deliver reliable notifications when reports are filed or errors occur

## 2  Agent Taxonomy, Sub-Tasks & Dependencies

### BusterOrchestrator
Coordinates message intake, report compilation, and submission flows.
*Sub-tasks*
- Dispatch messages to the ReportCompiler
- Manage user interactions and status updates

### ReportCompiler
Converts messages and link content into structured OFAC reports.
*Sub-tasks*
- Fetch and validate all linked media
- Aggregate user details and conversation history
- Produce standardized report JSON for DataValidation

### DataValidation
Ensures all required fields are present and formatted correctly.
*Sub-tasks*
- Run schema checks on compiled report data
- Flag missing or malformed information for remediation

### BestPractices
Captures policy guidelines for high-quality submissions.
*Sub-tasks*
- Apply scoring rules to evaluate completeness
- Recommend improvements before final filing

### 2.1 Buster Report Builder & Scoring Catalogue
- **Report Compiler** – builds the report payload
- **Report Scoring** – rates report completeness
- **Best Practices** – maintains OFAC compliance tips
- **Final OFAC Score** – combined quality metric

## 3  Agent Interface & Runtime Guarantees
The agent exposes a Discord slash command interface. All actions provide deterministic responses with clear error messages. Reports are persisted for audit.

## 4 Specification & Result Objects
Report objects follow an internal JSON schema containing message text, user identifiers, evidence URLs, timestamps, and scoring metadata.

## 5 Lifecycle & Orchestration Flow
1. User issues a report command
2. BusterOrchestrator gathers conversation context
3. ReportCompiler fetches and assembles data
4. DataValidation verifies schema compliance
5. BestPractices scores the report
6. Final report is filed with OFAC and logged

## 6 Coding, Testing & Deployment Standards
- Code style: PEP8 with 100 character lines
- Use `pytest` for automated tests
- Validate code with `flake8`
- Deploy via GitHub Actions to a containerized runtime

## 7 Continuous Intelligence & Self-Improvement (Learning Loop)
### 7.1 Data Flow
All filed reports and outcomes are logged for future training.
### 7.2 OFAC Best Practices Engine
Guides report improvements from past data.
### 7.3 ML Optimiser
Suggests new scoring rules based on historical success.
### 7.4 Planner Integration
Orchestrates advanced workflows if additional evidence is needed.
### 7.5 Auto-A/B & Drift Guard
Monitors performance changes over time and rolls back when needed.
### 7.6 Outcome Metric
Primary metric is successful OFAC report acceptance rate.

## 8 Security & Compliance Guardrails
- Sanitize all user input
- Store sensitive tokens securely
- Log access and report submissions for auditing

## 9 Deployment & Architecture Dependencies
- Docker image with Python runtime
- Access to Discord API and OFAC submission endpoint
- GitHub Actions for CI/CD

## 10 Contribution Workflow
1. Fork and create feature branch
2. Ensure `flake8` and `pytest` pass
3. Submit pull request for review

## 11 Leveraging System Intelligence to Transform Any Custom Prompt into a High-Success OFAC Violation Report
### 11.1 Data Assets We Exploit
Conversation logs, external links, and previous report outcomes.
### 11.2 Tactic Retrieval & Ranking Workflow
Retrieve evidence, rank by relevance, and compile.
### 11.3 End-to-End Prompt-to-Report Pipeline
From user command to final OFAC submission with scoring feedback.
### 11.4 Iterative Optimisation Loop (per request)
Refine reporting approach using scoring metrics and user feedback.
### 11.5 API Entry Points & Integration Hooks
Discord commands and HTTP endpoints for internal tools.
### 11.6 Security & Ethical Safeguards
Prevent abuse by enforcing content validation and access controls.
### 11.7 Outcome Guarantee
Aim for consistent, properly formatted submissions accepted by OFAC.

## 12 Repository Organization & Governance
### 12.1 Canonical Directory Layout
- `src/` – bot source code
- `tests/` – automated tests
- `docs/` – documentation
### 12.2 Logging & Observability Standards
Use structured logging with log levels for troubleshooting.
### 12.3 Separation of Concerns Rules
Keep orchestrator, compiler, validation, and best-practice logic modular.
### 12.5 File & Folder Hygiene
No large binaries in repo; use Git LFS if needed.
### 12.6 Governance Workflow
PR reviews required for all changes.
### 12.7 Automated Enforcement
CI pipeline runs `flake8` and `pytest` on each commit.

## 13 Detailed System Architecture

Below is the recommended file and module layout for a full Buster deployment. Each component maps
directly to one of the agents or support utilities described above.

```
src/
  buster/
    __init__.py
    discord_bot.py        # entrypoint, Discord command registration
    orchestrator.py       # implements BusterOrchestrator logic
    compiler/
      __init__.py
      report_compiler.py  # fetch messages and links, build report data
    validation/
      __init__.py
      schema.py           # JSON schema definitions
      data_validation.py  # DataValidation checks
    best_practices/
      __init__.py
      scoring.py          # scoring and compliance advice
      guidelines.py       # reference best-practices documentation
tests/
  test_orchestrator.py
  test_compiler.py
  test_data_validation.py
  test_best_practices.py
docs/
  architecture.md         # high level diagrams and design notes
  usage.md                # instructions for running the bot
  ofac_schema.json        # canonical OFAC report schema
AGENTS.md
README.md
requirements.txt
```

This layout keeps orchestrator, compiler, validation logic and best-practice rules in separate
modules while grouping them under a single package for clarity. Tests live alongside the code they
exercise, and all documentation resides in the `docs/` directory.

# Buster Agent Service Documentation

## OFAC Reporting Best Practices

# Preparing an OFAC Sanctions Violation Report or Voluntary Self-Disclosure (VSD): Standards & Best Practices

## 1. Cover Letter

Begin the submission with a concise cover letter that identifies the disclosure and provides key reference information. This sets the stage for OFAC's review and clearly flags the nature of the submission:

**1.1 Voluntary Self-Disclosure Statement:** State upfront whether the submission is a **Voluntary Self-Disclosure (VSD)** or a mandatory report. OFAC considers a valid VSD a significant mitigating factor – a qualifying VSD can result in a 50% reduction of the base civil penalty. If the disclosure is voluntary, explicitly say so in the first paragraph (e.g., "This is a Voluntary Self-Disclosure under OFAC's Enforcement Guidelines") to ensure OFAC recognizes it. If the report is being submitted in response to an OFAC subpoena or other requirement (i.e. not voluntary), clarify that instead. According to OFAC's guidelines, a voluntary self-disclosure should include a report with **"sufficient detail to afford OFAC a complete understanding of an apparent violation's circumstances"** – the cover letter can signal that such detail is enclosed.

**1.2 Identification of Applicable Sanctions Program(s) and Legal Authorities:** Identify which **sanctions program(s)** and legal authorities are implicated by the apparent violation. For example, note if it involves the **Iranian Transactions and Sanctions Regulations (ITSR)** under the International Emergency Economic Powers Act (IEEPA), the **Specially Designated Nationals (SDN) List**, or specific Executive Orders. Citing the relevant regulations and laws (with sections) up front helps OFAC route the case appropriately and frames the legal context. It also demonstrates that the reporting entity understands which sanctions rules were violated. If multiple programs or statutes apply, list each (e.g., Iran and Syria sanctions programs, violations of 31 C.F.R. part 560, and Executive Order X). This section of the cover letter essentially answers "what law was broken" and under which authority, giving OFAC the legal footing of the submission.

**1.3 Case/Reference Number:** If OFAC has already opened an inquiry and provided a case ID or reference number, include it prominently. This could be in the subject line and again in the body (e.g., "Re: Case ID ####"). Tying the report to an existing OFAC case number ensures it gets integrated into the correct enforcement file. If no case number exists (for instance, a purely voluntary disclosure not prompted by OFAC), state that this is an initial disclosure and no case number has been assigned yet.

**1.4 Primary Point of Contact:** Provide contact details for the person responsible for correspondence on the submission. Include the **name, title, organization, telephone, and email** of the primary point of contact (e.g., the compliance officer or legal counsel overseeing the matter). OFAC often has follow-up questions, and listing a knowledgeable individual for them to reach out to facilitates communication. This person should be readily available to respond to OFAC and coordinate any supplemental submissions. It's also wise to note in this section if the submission is made by outside counsel on behalf of the company, and if so, that counsel's contact information.

*(The cover letter should be signed by an authorized person, such as a senior compliance officer or counsel, to attest to the sincerity of the disclosure. It is effectively the formal transmittal of the report.)*

## 2. Executive Summary

Provide a high-level **Executive Summary** of the violation and its significance. This section distills the entire submission into a few key points for quick understanding:

**2.1 Key Facts (Who, What, When, Where, Value):** Summarize the core facts of the apparent violation in a few sentences. Identify **who** was involved (the company and any relevant business units or personnel, as well as the counterparties or sanctioned parties), **what** happened (the nature of the transaction or activity that violated sanctions), **when** it occurred (the date(s) or time frame of the violation), **where** it took place (jurisdictions or locations, if relevant), and the **value** of the transactions or assets involved. This concise synopsis gives OFAC an immediate snapshot of the case context. For example: "Between January and March 2024, XYZ Corp (a U.S. manufacturer) shipped three orders of industrial equipment to a distributor in Country Z, which were ultimately destined for a company 50% owned by an SDN – an apparent violation of Iran sanctions, with a total value of $2.5 million." Including the **approximate dollar value** is important because the transaction value often factors into penalty calculations. The goal is to present the violation's outline so that even a reader skimming the report understands the essence of the issue.

**2.2 Overall Impact and Potential Harm:** Describe in broad terms the **impact or harm** of the apparent violation. This could include the potential harm to U.S. foreign policy or national security objectives (e.g. funds or goods reaching a sanctioned regime or prohibited end-user), as well as the company's own assessment of the seriousness. For instance, note if the violation was *isolated and self-contained* or *systemic*, and whether it caused any actual transfer of significant value or merely a technical paperwork lapse. OFAC's enforcement response often considers the harm to sanctions program objectives – so an executive summary should indicate if, say, the violation allowed a blocked person to receive economic resources (a higher harm scenario) or if controls failed but funds were ultimately blocked (mitigated harm). If applicable, mention any **mitigating circumstances** upfront – for example, if the issue was discovered internally and no other parties were harmed, or if the value was very low. Conversely, if this disclosure involves a **large volume of transactions or a long-running scheme**, the summary should acknowledge the scale. Conclude the executive summary with the **requested disposition** or why the submitter believes mitigation is warranted (e.g., "We respectfully request OFAC consider the voluntary self-disclosure and prompt remedial actions described herein and treat this matter as appropriate for a cautionary letter or settlement at the lower end of the guidelines range"). This foreshadows the desired outcome, such as a reduced penalty or a finding of violation instead of a monetary penalty, setting a tone for mercy by highlighting voluntary cooperation.

## 3. Reporting Entity Information

This section provides OFAC with a clear understanding of **who is making the disclosure** – the company or individual involved – and their business profile. It helps OFAC contextualize the violation within the entity's operations and compliance structure:

**3.1 Legal Name, Address, and Corporate Details:** Give the full **legal name of the reporting entity**, its primary business address (headquarters), and identifying information like Employer Identification Number (EIN) or DUNS number. Describe the entity's place within any **corporate family** – for example, if it is a subsidiary of a larger parent company, or if it has multiple affiliates. This can include an overview of corporate structure (you may reference an organizational chart in the exhibits). The goal is to leave no ambiguity about who the disclosing party is and to help OFAC determine if this entity has been involved in past enforcement cases or has related entities that are relevant.

**3.2 Lines of Business and Geographic Footprint:** Briefly explain what the company (or individual, if applicable) does: its main **lines of business**, industry sector, and the regions/countries in which it operates. This is important for OFAC to gauge the sanctions risk exposure. For instance, a fintech payment processor operating globally will have different risk considerations than a local manufacturing firm. Mention key markets and any high-risk areas (e.g., significant business in or with high-risk jurisdictions, if relevant to the case). This context can shed light on how the violation occurred (e.g., a company with extensive Middle East operations might have more sanctions exposure). It also demonstrates transparency by voluntarily offering information about the company's scope.

**3.3 Senior Management Sign-Off / Authorized Signatory:** Indicate that the report has been reviewed and approved by senior management, and include the name and title of the **executive or officer who is signing the submission**. OFAC expects that companies involve upper management in compliance matters; a management-level signatory underscores that the company takes the issue seriously and is committed to remediation. For example, note that the CEO, General Counsel, Chief Compliance Officer, or other high-ranking official has authorized the disclosure. This can be combined with the certification section (see Section 10), but it's worth mentioning here as part of the entity overview that leadership is engaged. A best practice is to include a statement that *"Senior management has reviewed the findings of the internal investigation and this disclosure report,"* reflecting a top-down commitment to address the violation.

*(Providing this background information in Section 3 helps OFAC understand the scale and sophistication of the reporting entity. Smaller companies might need to explain resources and compliance infrastructure, whereas larger institutions should delineate which division or affiliate was involved. This also lays groundwork for later sections about compliance program and remedial measures.)*

## 4. Apparent Violation(s) — Detailed Narrative

This section is the **heart of the report**, where you provide a detailed, step-by-step narrative of what happened. It should be organized clearly and cover all factual and legal aspects of the apparent violation. The narrative needs to be thorough enough to meet OFAC's requirement for a report that affords a *"complete understanding of an apparent violation's circumstances"*. It often makes sense to break this section into sub-parts for clarity:

**4.1 Chronology of Events (Discovery through Present):** Tell the story of the violation in chronological order. Begin with how the issue was **discovered** (e.g., through an internal audit, a compliance screening hit, a whistleblower report, etc.), then walk through the sequence of events up to the present. Include dates and timeframes for key events: when the transactions occurred, when compliance staff or management first became aware of the potential problem, any immediate actions taken upon discovery, and subsequent investigation milestones. This timeline helps OFAC see the progression from violation occurrence to detection and disclosure. For example, "On March 1, 2025, the compliance department identified a sanctions screening alert related to a payment. Upon investigation, it was found that…". Make sure to clarify **who did what at each stage** – e.g., "the trade compliance manager halted further shipments on April 5, 2025, after confirming the goods had been sent to a blocked entity." A clear chronology demonstrates diligence and transparency, showing OFAC that the company has reconstructed the issue comprehensively.


**4.2 Transaction-Level Facts:** For each transaction or activity that violated (or apparently violated) the sanctions, provide granular details. OFAC will need to know the **specifics of each transaction**, so include at minimum:

* **Date and Settlement Date:** The date when the transaction occurred, and if different, the settlement/clearing date for payments or delivery date for shipments. Precise dating helps OFAC tie violations to specific sanction program periods or designation dates.
* **Counterparties and Their Roles:** Identify all parties involved in the transaction and their roles – e.g., the customer, supplier, financial institutions, agents, shipping companies, beneficiaries. Include full names and locations of these parties, and note any ownership or affiliation relevant to sanctions (for instance, if a counterparty is 50% owned by an Iranian entity). Clarify who the **sanctioned party** is (if one is involved) – e.g., "Counterparty X was the buyer and is owned by an SDN; Counterparty Y was an intermediary freight forwarder."
* **Financial Routing Details:** Provide details on how funds or goods moved. For payments, include bank names, account numbers, and **SWIFT message references** or payment instructions that show the path of funds. If the transaction was in cryptocurrency or digital assets, include **transaction hashes and wallet addresses** for both senders and receivers. This level of detail allows OFAC to trace the flow of funds or shipments and verify involvement of any U.S. financial system elements.
* **Commodity/Service Description and Value:** Describe what was transacted – the **goods, technology, or services** involved – with as much specificity as possible. Include the quantity and **approximate value** of each transaction (both in the original currency and U.S. dollar equivalent). For shipments, reference invoice numbers, product descriptions, HS codes (if relevant), etc. For financial services, describe the type of transfer. Providing the **valuation in USD** along with original currency and exchange rates used is a recommended practice. This not only helps OFAC assess the scope of the violation, but is also required for proper penalty calculation (since penalties are often based on the dollar value of transactions).

Each transaction can be labeled (e.g., "Transaction 1," "Transaction 2," etc.) and cross-referenced with evidence in the Exhibits (Section 12) such as invoices, wire transfer records, bills of lading, or blockchain transaction printouts. The narrative here should be factual, sticking to what happened, and avoid legal argument – save any arguments or mitigation points for later sections. If there were multiple transactions of a similar nature, you might summarize them collectively but still provide a breakdown in a table or exhibit. The key is that **OFAC can understand exactly what transpired, who was involved, and how it violated specific sanctions regulations**.

**4.3 Statutory/Regulatory Provisions Breached:** Identify which **specific sanctions regulations** or Executive Orders were violated by the described conduct. This ties the facts to the law. For example, "These transactions appear to violate § 560.204 of the ITSR (prohibition on export of services to Iran) as well as Executive Order 13xxx." If multiple provisions apply (common in complex cases), list all relevant citations. Also mention the **legal authority** (e.g., IEEPA) under which those regulations were issued, because penalty calculations and maximums can depend on the statute. Including this legal analysis shows OFAC that the company has done its homework in understanding the infraction. It's also where counsel's input is crucial – ensure the correct provisions are cited. In some cases, it might be an **OFAC general license violation** or a violation of **specific license terms**; mention that as well if applicable. Essentially, this sub-section answers "which OFAC rules did we break, and how." This will correspond to the violation type that OFAC eventually characterizes the case as (e.g., an "apparent violation of the North Korea Sanctions Regulations, § 510.X"). Being precise and upfront about this can be seen as part of cooperation and candor.

**4.4 Knowledge & Intent:** Describe **how and when the company and relevant employees first became aware** of the potential violation, and discuss whether the violation was inadvertent, negligent, or willful. OFAC's enforcement response heavily weighs the violator's state of mind – willful or reckless violations are treated far more severely than mistakes or lack of awareness. In this section, clarify if the actions were the result of an oversight, a misunderstanding of the law, or deliberate evasion. For example, "The employee in charge of exports was not aware that the customer's parent company was on the SDN List" versus an intentional scenario. Include any evidence of internal discussions or warnings that were ignored (if unfortunately there are any), as that will come out in investigation anyway. If the violation was **inadvertent or due to a screening gap**, state that and explain that there was no intent to violate sanctions. If any **red flags** were missed, acknowledge them and note at what point they were recognized. Conversely, if an investigation found an employee acted willfully against policy, that's critical to disclose (with counsel's guidance on how to present it). Demonstrating a candid accounting of knowledge and intent – even if it involves employee misconduct – can support the case that the company itself is coming clean and did not condone the behavior. It's also important to note **when management learned of the violation**: e.g., "Senior management became aware of the issue on Date X during an internal audit" – showing that once they knew, they took action (to be detailed in later sections). Essentially, this sub-section aligns with General Factors A and B of OFAC's Enforcement Guidelines (willfulness/recklessness and awareness of conduct), so addressing it in the report is crucial.

**4.5 Pattern-or-Practice Analysis:** Indicate whether this violation appears to be a **one-off incident or part of a broader pattern**. OFAC will want to know if the apparent violation is isolated or if similar compliance breakdowns have happened before. If the internal investigation found other instances or a systemic issue, summarize that here (and you will likely include additional instances in the transaction details if needed). For example: "Our review determined that these three transactions were the only ones involving this blocked party – no broader pattern of misconduct was identified" **or**, "The investigation revealed two earlier similar payments that also potentially violated sanctions, indicating a broader gap in controls, which are being addressed." If the company has any **history of sanctions issues** (past cautionary letters, prior voluntary disclosures, or enforcement actions), it may be relevant to mention or at least allude to them here or in the compliance history section (Section 7.3). OFAC's penalty guidelines provide extra mitigation for a *"first violation"* and conversely will consider past violations or patterns as aggravating. Therefore, being upfront about whether this is the first known breach or part of a recurring issue is important. If it's truly the first, emphasize that (and that a thorough review didn't find other violations). If not, explain the context of the past incidents and whether they were previously disclosed or resolved. The goal is to show OFAC that you have looked for any **"pattern or practice"** of non-compliance – which demonstrates thoroughness – and to position the disclosed violation in the correct context of frequency/severity.

*(The detailed narrative in Section 4 should be well-organized and as factual as possible. It may span multiple pages if needed. Use clear subheadings for each sub-part (chronology, transaction details, etc.) and consider tables for any repetitive data. Also, when writing the narrative, avoid legal argument or justifications here – save those for mitigation sections. Keep this section objective. Cite to exhibits (by exhibit number) for key facts, e.g., "See Exhibit 5 for a copy of the SWIFT payment message.")*

## 5. Root-Cause & Risk Assessment

In this section, explain **why the violation happened** – identifying the root causes within your organization's processes or external factors. This shows OFAC that you not only identified what went wrong, but also *why*, which is critical for prevention. It demonstrates a level of self-analysis and accountability that OFAC looks for in cooperative disclosures.

**5.1 Breakdown of Screening, KYC, or Control Failures:** Provide an analysis of the compliance control failure that allowed the violation. Was it a **screening error** (e.g., a name match was missed due to spelling variation), a deficiency in **Know-Your-Customer (KYC)** procedures (e.g., failure to identify an ultimate beneficial owner who was sanctioned), human error, or perhaps a gap in automated systems? For example, "The root cause was a configuration error in our sanctions screening software, which failed to flag the SDN's alias," or "The sales department bypassed the usual export control review due to rush shipment pressures." Be candid and specific – OFAC will gauge your compliance program's adequacy in part by how well you identify and address the failure. If multiple breakdowns occurred, list each (perhaps as bullet points): e.g., training gaps, lack of escalation of red flags, unclear policy on certain payment types, etc. The aim is to show **exactly how the sanctioned party or destination slipped through your safeguards**. In doing so, you're effectively laying the groundwork for the remedial measures in Section 8 by identifying what needs fixing. This analysis should tie back to the facts: for instance, "Counterparty XYZ was not recognized as 50% SDN-owned because our screening only captured direct matches, not ownership; this has been identified as the primary control failure."

**5.2 Contributing External Factors:** Acknowledge any **external complexities or factors** that contributed to the violation. Sometimes sanctions evasion tactics by counterparties play a role, or complex corporate structures obscure sanctioned ownership. For example, "The sanctioned party used a layered ownership structure through three shell companies, making detection difficult," or "Rapidly changing sanctions (the counterparty was added to the SDN List just one day before the transaction) contributed to the oversight." While not shifting blame, it is useful to note if **external conditions** like evolving sanction regimes, sophisticated evasion schemes, or ambiguous identities contributed to the issue. This demonstrates to OFAC that the company understands the broader risk environment. For instance, in the fintech or crypto space, one might note that the use of **privacy wallets** or mixers obscured the ultimate recipient. In shipping, one could mention that vessels turned off AIS (Automatic Identification System) or falsified documents – tactics highlighted in OFAC's maritime advisories. By highlighting such factors, you contextualize the violation (it wasn't sheer negligence; there were complicating factors) while still accepting responsibility for missing them. If none, that's fine – then the cause was purely internal.

**5.3 Materiality Analysis:** Discuss the **materiality** of the violation in terms of transaction value, volume, and overall risk. Was this a small-dollar, low-impact violation or a significant breach? OFAC will consider whether the violation was *"egregious"* or not, which involves the scale and impact (among other factors). If the total value was low or the transactions few, point that out as mitigating (but do so factually: e.g., "Total value of all identified apparent violations was $50,000, involving two transactions"). If the value was high or many transactions were involved, acknowledge that scale and perhaps break down the numbers (the Excel attachment in Exhibits will detail transaction by transaction, but here you might sum it up). Also consider the **jurisdictions** and counterparties: dealing with a comprehensively sanctioned country (like North Korea) might be viewed as more severe than, say, an SDN who is not part of a broader program – explain where this falls. This analysis can feed into why the violation might be considered non-egregious (if it is small and promptly corrected) or, if it's larger, it sets the stage for emphasizing your strong cooperation and remediation to offset the severity. Essentially, you are demonstrating that you have assessed how serious the issue is from a sanctions policy perspective, which is something OFAC itself will do. If relevant, note any **loss to sanctioned persons prevented** (e.g., funds were blocked and not released, mitigating the harm). Summarize the magnitude: number of transactions, total value, over what period – this gives OFAC a quantified sense of the problem.

*(The Root Cause analysis in Section 5 shows OFAC that you've done a **critical self-examination**. OFAC's Enforcement Guidelines Factor F (Remedial Response)and Factor E (Compliance Program effectiveness) both relate to understanding what went wrong and fixing it. By clearly articulating root causes, you set up a credible narrative that you can and will address these issues.)*

## 6. Internal Investigation Methodology

This section explains *how* you conducted the internal review that underpins the disclosure. It gives OFAC confidence that the disclosure is complete and reliable. Being transparent about your investigative steps and scope is part of demonstrating cooperation and thoroughness.

**6.1 Scope, Tools, and Time Frame:** Describe the **scope of the internal investigation**. For example, did it cover all business units and affiliates or was it focused on a specific division? State the **time frame** reviewed (e.g., transactions from 2022-2024 were reviewed for any similar violations). Mention the **tools and techniques** used: e.g., transaction screening software, email keyword searches, blockchain analysis tools, forensic accounting, etc. If outside counsel or a forensic firm was engaged, you can note that as well ("with the assistance of an external forensic investigations team, we analyzed...") without waiving privilege on the content. This subsection essentially conveys that the company took the investigation seriously by dedicating resources and expertise to uncover the full extent of the issue. Also, clarify the **timeline** of the investigation – e.g., "The internal review was initiated on July 1, 2025, and substantively completed by September 30, 2025, covering all transactions from 2020 to 2025." Highlight if it was a *comprehensive review* (which OFAC will appreciate as cooperation) or a targeted one (if limited, explain why it sufficed). Emphasize any data analytics or special measures (for instance, scanning all customers against the SDN List retroactively).

**6.2 Custodians Interviewed / Data Sources Searched:** Provide an overview of **who and what was examined**. "Custodians" here means employees or data repositories. For example, list the key **personnel interviewed** (titles or roles, not necessarily names unless you choose) – e.g., the sales manager involved, compliance analysts, etc. – and note that detailed interview memos are available if needed. Also list **data sources** reviewed: email archives, chat logs (e.g., internal messaging like Slack or Bloomberg chat if a bank), business unit shared drives, physical documents, transaction databases, etc. Essentially, show that you looked everywhere relevant. For instance: "We collected and reviewed approximately 10,000 emails from the custodians directly involved, including the export team and compliance department, to identify any discussions of the transactions or sanctions concerns." If any third-party records were obtained (like from partner banks or freight forwarders), mention that cooperation (this overlaps with Section 9.3 on third-party cooperation). Detailing this breadth of sources underscores thoroughness. You want OFAC to be confident that no stone was left unturned – that this disclosure isn't just the tip of an iceberg, unless you're affirmatively disclosing the whole iceberg. If some sources couldn't be searched (e.g., data was lost or a person left the company), note what you did to mitigate that (attempted recovery, etc.). This level of transparency will bolster your credibility.

**6.3 Preservation of Evidence & Privilege Protocol:** Summarize how you **preserved relevant data** and maintained privilege where appropriate. For example, note if legal hold notices were issued to relevant employees to prevent deletion of emails or documents once the issue was identified. OFAC will appreciate knowing that once the company discovered the issue, it took steps to preserve evidence (this is part of good faith cooperation). Additionally, mention if outside counsel directed the investigation, which might indicate certain materials are covered by attorney-client privilege or work product. It's wise to strike a balance: you don't need to list every detail of legal strategy, but you can state, for instance, "Under the direction of counsel, the company preserved all relevant communications and records. Interview summaries were prepared by counsel and are being submitted with appropriate privilege markings." OFAC in its guidance doesn't explicitly require details on privilege, but compliance professionals often include a note that privileged materials are being withheld or provided in a certain manner. Also, if you are providing any privileged documents (sometimes companies waive privilege for mitigation credit), state the terms of that (though usually it would be coordinated with OFAC separately). The key message in this sub-section is: **we did not destroy or withhold evidence**, and we managed sensitive information properly. You can also mention if the company entered into a **tolling agreement** with OFAC to pause the statute of limitations, as that is often seen as a cooperative step (though that might also be mentioned in Section 9.1). Indeed, OFAC's guidelines count extending a tolling agreement as a factor in cooperation, so disclosing that you've done so (if applicable) is helpful.

*(Overall, Section 6 demonstrates that the disclosure is backed by a robust internal investigation. It helps preempt OFAC's questions about whether all relevant facts have been uncovered. If the methodology is sound, OFAC can trust the findings and scope described in the narrative and exhibits.)*

## 7. OFAC Compliance Program (at Time of Violation)

Here, provide a snapshot of what your **sanctions compliance program** looked like at the time the violation occurred. OFAC will evaluate the adequacy of your program *at the time of the breach* as part of its enforcement deliberations. This section allows you to show that either (A) you had a program (though it had a gap, now fixed), or (B) if you lacked a robust program, you acknowledge it and have since improved it (to be detailed in Section 8).

**7.1 Policy Architecture (Governance, Risk Assessment, Testing):** Describe the overall **structure of your sanctions compliance program** in place when the violation happened. This includes governance (who was responsible for OFAC compliance – e.g., a dedicated sanctions officer or committee?), risk assessment processes (did the company periodically evaluate its sanctions risks?), and testing/audit routines (was there an internal audit or testing of sanctions controls). For example, note if you had written OFAC compliance policies or manuals, what the reporting lines were (did compliance report to the General Counsel or Board?), and whether sanctions compliance was integrated into enterprise-wide risk management. If the company uses a **risk-based approach** (as OFAC expects), briefly describe how it identified higher-risk activities. OFAC's **Framework for OFAC Compliance Commitments** outlines five essential components of a sanctions compliance program (management commitment, risk assessment, internal controls, testing, training). You can align with those in explaining what existed. Emphasize positive elements (if any) like "Company XYZ had an OFAC screening policy that required all new customers to be screened against the SDN List and all payments to be checked," or that "regular training was provided to staff." However, be candid about any **gaps at the time** (since a violation did occur). This section isn't to make excuses, but to inform OFAC's understanding of the context – e.g., maybe the company's program was solid on paper but a specific control failed, or maybe the program was in early stages of maturity.

This includes governance (who was responsible for OFAC compliance – e.g., a dedicated sanctions officer or committee?), risk assessment processes (did the company periodically evaluate its sanctions risks?), and testing/audit routines (was there an internal audit or testing of sanctions controls). For example, note if you had written OFAC compliance policies or manuals, what the reporting lines were (did compliance report to the General Counsel or Board?), and whether sanctions compliance was integrated into enterprise-wide risk management. If the company uses a **risk-based approach** (as OFAC expects), briefly describe how it identified higher-risk activities. OFAC's **Framework for OFAC Compliance Commitments** outlines five essential components of a sanctions compliance program (management commitment, risk assessment, internal controls, testing, training). You can align with those in explaining what existed. Emphasize positive elements (if any) like "Company XYZ had an OFAC screening policy that required all new customers to be screened against the SDN List and all payments to be checked," or that "regular training was provided to staff." However, be candid about any **gaps at the time** (since a violation did occur). This section isn't to make excuses, but to inform OFAC's understanding of the context – e.g., maybe the company's program was solid on paper but a specific control failed, or maybe the program was in early stages of maturity.

**7.2 Automated Screening Systems & Escalation Procedures:** Go into detail on the **technical and procedural controls** relevant to the violation. Most importantly, describe your **sanctions screening system** (if the violation involved a blocked party name or prohibited country that should have been screened). What screening tool was in use? Was it updated with the latest OFAC list? Did it include fuzzy matching, and was it properly configured? Also, outline the **escalation process**: when a potential hit or red flag arose, what was supposed to happen? For example, "Potential SDN name matches were referred to the Compliance Department Level 2 analysts for review" or "Country-of-origin red flags in orders would prompt legal review under export controls." If the violation circumvented these, explain how (as done in Root Cause section). It's also good to mention any **transaction monitoring systems**, interdiction software, or other relevant fintech tools. If relevant, describe procedures like how blocked property was handled. This section gives OFAC a sense of the day-to-day operational compliance measures that were (or weren't) in place. It also highlights whether the violation was a one-time fluke vs. a sign of systematic control issues. If your program was generally strong but this violation revealed a narrow gap, emphasize that strength (and that the gap is now fixed). If the program was weak, acknowledge it here, because Section 8 will describe remediation.

**7.3 Prior Enforcement History (if any):** Disclose any prior encounters with OFAC enforcement or other relevant regulatory actions related to sanctions. This could include past voluntary disclosures, warning letters, cautionary letters, settlements, or even close calls that didn't result in action. OFAC will likely know if they have formally taken action in the past five years (and under the Enforcement Guidelines, a "first violation" gets extra mitigation, whereas a repeat issue is aggravating). So it's better you state it upfront. For instance, "This is the first sanctions-related issue the company has identified or disclosed," or "The company received a cautionary letter in 2019 regarding a smaller OFAC screening lapse, which prompted improvements at that time." If you've never had any enforcement or inquiries, you can say the company has no history of sanctions violations. If the company is part of a larger corporate group and another affiliate had an OFAC case, mention that for completeness if relevant. Keep this section factual.

*(Section 7 allows you to **"show your work"** on compliance efforts around the time of violation. OFAC likes to see that a company isn't a bad actor ignoring sanctions entirely. Even if the program had shortcomings, demonstrating that some structure was in place (and now being improved) is useful. Conversely, if no program existed, admitting that and emphasizing the changes being made will be important.)*

## 8. Corrective & Remedial Actions
This section details the **actions taken to address the violation and prevent future occurrences**. It's one of the most critical parts of the submission for demonstrating that the company is proactive and responsible.

**8.1 Immediate Containment Measures:** Describe what you did **immediately upon discovering** the violation to stop any further potential breaches. Did you halt certain transactions or shipments? Did you block or freeze any funds that were in transit to a sanctioned party? For example, "On discovery, the compliance team **blocked the pending wire transfer** to the SDN account, preventing its completion," or "All further deliveries to the distributor were suspended." If the violation involved ongoing activity, assert that you **ceased the conduct promptly**. Also mention any notifications to other parties. The aim is to show OFAC that you acted quickly to contain and limit any harm.

**8.2 Enhancements to Policies, Screening Tools, Training, Staffing:** Detail the **improvements to the compliance program** that have been implemented (or are in progress) as a result of this incident.
* **Policies and Procedures:** Note any updates to written policies or manuals.
* **Screening/Technology:** If a tech control failed, describe the fix or upgrade.
* **Training and Awareness:** Note any new training programs or refreshers conducted.
* **Personnel/Resources:** Mention if you added compliance staff or reorganized responsibilities.

**8.3 Disciplinary Action and Enterprise-Wide Lessons:** Explain if any **disciplinary measures** or personnel actions were taken in response to the violation, and how lessons learned have been communicated across the organization.

**8.4 Commitment to Ongoing Cooperation:** Reiterate how you will continue to **cooperate with OFAC** until the matter is fully resolved. Mention if a **tolling agreement** was offered or if you anticipate providing supplemental information.

*(Section 8 is often scrutinized by OFAC to determine how much credit to give for remediation. A strong showing here can significantly tip the outcome toward a cautionary or minimal penalty, especially in conjunction with voluntary disclosure.)*

## 9. Cooperation and Mitigating Factors

In this section, explicitly highlight how the disclosure and the company’s actions exemplify **cooperation** and other mitigating factors.

**9.1 Timeliness and Voluntariness of the Disclosure:** Emphasize that the disclosure was **prompt and voluntary** if true.

**9.2 Extent of Document Production and Data Provided:** Detail the **breadth and depth of information** you’ve given to OFAC, underlining your cooperation.

**9.3 Third-Party Cooperation (Banks, Business Partners):** Mention the company’s efforts to involve and cooperate with any third parties.

*(By enumerating these cooperation points, you clearly map your actions to OFAC’s mitigating factors.)*

## 10. Certification & Attestation

Include a **certification of accuracy and completeness**, signed by a responsible officer.

**10.1 Accuracy and Completeness Statement:** Provide a sentence attesting that the submission is true, accurate, and complete, possibly under penalty of perjury.

**10.2 Signature, Date, and Title of Signatory:** Leave space for the **signature** of the certifying official, along with the date, name, and title.

*(This certification section, while brief, is important for completeness.)*

## 11. Index of Exhibits

Provide a **numbered index or list of all exhibits/attachments** that accompany the narrative report.

## 12. Exhibits / Attachments

After the index, include **all supporting documents** as exhibits. Label each exhibit and Bates-number sequentially across the submission.

---

#### Formatting & Technical Tips (Condensed from OFAC’s July 2024 Submission Standards)

* **Single, Combined PDF for Narrative:** Provide the main narrative as a single PDF.
* **Native Format for Data Tables:** Submit voluminous data in a **native format like Excel** rather than PDF.
* **Large File Submissions:** Use the **OFAC Secure File Transfer Portal** for packages over about 150 MB.
* **Encryption and Passwords:** Encrypt or password-protect the files and provide the password separately.
* **File Naming and Labeling:** Clearly name your files with the company name, submission date, and, if applicable, case number.
* **Avoiding Technical Pitfalls:** Ensure all PDFs are text-searchable and coordinate with OFAC if unusual formats are involved.

### Why This Outline Works

* **Substantive Completeness:** The sections mirror the elements OFAC asks for in a disclosure.
* **Mitigation-Ready Presentation:** The structure surfaces the factors that can lead to penalty mitigation.
* **E-Discovery Discipline:** By adhering to OFAC’s preferred formatting, the outline integrates e-discovery best practices.

Use this outline as a flexible template, tailoring it to the size and complexity of the case. Always have legal counsel review the final report.

## Industry-Specific Considerations

### Fintech & Digital Payments
Highlight the use of API-based sanction screening, transaction monitoring tailored to the platform, and cooperation with partner banks. Include a detailed transaction log when many small payments are involved.

### Maritime Shipping
Include vessel names, routes, and cargo details. Emphasize coordination with maritime insurers and port authorities.

### Cryptocurrencies and Virtual Assets
Provide wallet addresses and transaction hashes. Note any use of blockchain analytics tools and cooperation with law enforcement.

### Manufacturing & Export Businesses
Detail the supply chain and distribution network. Discuss export control issues and due diligence on distributors.

### Defense & Arms Industry
Provide part numbers and intended versus actual end-users. Highlight coordination with State or Justice Department if relevant.

### Narcotics Trafficking & Illicit Finance
Discuss AML controls and any cooperation with law enforcement. Emphasize KYC enhancements and transaction monitoring improvements.

### High-Tech and Electronics
Map out the technology and its journey. Note any foreign subsidiaries involved and compliance with export controls.

