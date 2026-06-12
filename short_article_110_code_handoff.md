# How to Safely Handle a Code Handoff from an Agency

**Word Count:** ~600 words
**Target Keywords:** software code handoff, outsourcing transition, IT vendor handover

Whether you are migrating from one offshore agency to another, or transitioning an outsourced software product back to your internal in-house team, the "Code Handoff" is the most dangerous phase of the software lifecycle.

If an agency simply emails you a ZIP file containing the source code and walks away, you are in massive trouble. 

Without a rigorous handover process, your new developers will spend three months staring at confusing, undocumented code, unable to compile the application or fix basic bugs. To prevent your software from becoming "dead code," here is the mandatory checklist for a safe code handoff.

## 1. Secure the Intellectual Property (IP) First
Before the handover begins, verify that you actually own the code. Ensure you have administrative access to the primary code repository (usually GitHub or Bitbucket). 
The agency should not be pushing code to their own private servers; they must push it to a repository owned by your company's email domain. If the agency goes bankrupt tomorrow, you must have immediate legal and physical control of the raw source code.

## 2. Demand a "ReadMe" and Architecture Diagram
Developers hate writing documentation, so they often skip it. You must enforce it before the final invoice is paid.
* **The ReadMe File:** This is the manual for the code. It must explicitly state the exact software versions required to run the app (e.g., "Requires Node.js v18 and PostgreSQL v14"). It must include step-by-step instructions on how a brand-new developer can install the app on a blank laptop.
* **The Architecture Diagram:** Your new team needs a visual map. This map must show how the front-end talks to the back-end, where the API gateways are, and how the cloud servers (AWS/Azure) are configured.

## 3. The "Clean Room" Compile Test
Never accept the agency's word that "the code works." You must prove it.
Take a junior developer from your new team, give them a completely blank, wiped laptop, and tell them to follow the ReadMe instructions to download and start the application.

If the app fails to start on the blank laptop, it means the agency relies on hidden, undocumented configurations on their own machines. The agency must fix the documentation until the Clean Room test passes flawlessly.

## 4. Transfer of Secrets and Credentials
Your software relies on dozens of third-party services (Stripe for payments, Twilio for SMS, AWS for hosting). These services use "API Keys" (highly sensitive passwords).
If the agency set up these accounts using their own agency email addresses, they can shut off your app at any time. You must force the agency to transfer ownership of all cloud accounts and API keys to your company's master email address (e.g., admin@yourcompany.com). 

## 5. The Overlap Period
The best code handoffs are not an abrupt stop. You should negotiate a 2-to-4-week "Overlap Period." 
During this month, your new developers (or your new offshore team) take control of writing the code, but the old agency remains on a retainer as "consultants." If the new team gets stuck on a confusing piece of legacy logic, they can instantly ping the old agency for clarification.

A professional, high-quality offshore software agency will plan the offboarding and handover process with as much rigor as they planned the initial build, ensuring your business continuity is completely protected.
