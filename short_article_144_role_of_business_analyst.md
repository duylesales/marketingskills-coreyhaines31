# The Role of Business Analysts in Offshore Software Projects

**Word Count:** ~600 words
**Target Keywords:** software business analyst, IT outsourcing roles, software requirements gathering

A company hires an offshore development agency to build a custom HR portal. 
The CEO writes a one-paragraph email to the developers: *"We need a portal where employees can request time off, and managers can approve it. It should sync with our Google Calendars."*

The developers read the email, nod, and start coding. Three months later, the software is delivered. It technically does exactly what the CEO asked. But when the company tries to use it, it’s a disaster. 
*What happens if an employee requests time off, but then quits the next day?* The developers didn't code for that. The system crashes.
*What happens if a manager denies the request? Does the employee get an email?* The developers didn't build an email system, because the CEO didn't explicitly ask for it.

The project failed because there was a massive translation gap between the "Business Idea" and the "Technical Reality." The only way to close this gap in an outsourcing project is by deploying a **Business Analyst (BA).**

## What is a Business Analyst?
The Business Analyst is the ultimate translator. They do not write code, and they are not the CEO. They sit perfectly in the middle. 

Their job is to listen to the CEO’s grand, vague vision, and ruthlessly tear it apart by asking hundreds of hyper-specific, annoying questions. They uncover every single edge case, every potential error, and every hidden requirement. 

Once they have extracted the true business logic, they translate it into a language the developers understand: **Technical Tickets.**

## The Discovery Phase: The BA's Domain
When you engage a premium offshore software agency, the very first step is the "Discovery Phase." The BA takes total control of this phase.

They do not accept a one-paragraph email. They will run workshops with your team. 
If you say, "I want a button that charges the customer's credit card," the BA will ask:
* *"What payment gateway are we using? Stripe or Braintree?"*
* *"What happens if the card is declined? Do we show a generic error, or do we tell them they have insufficient funds?"*
* *"If the payment succeeds, do we generate a PDF receipt? If so, does it need to include VAT taxes for European customers?"*

## Writing the Blueprint (User Stories)
After interrogating the business stakeholders, the BA writes the actual blueprints for the software, usually in the form of "User Stories" and "Acceptance Criteria." 

Instead of a vague email, the BA creates a Jira ticket for the developer that looks like this:
**User Story:** *As a Manager, I want to click 'Deny' on a time-off request, so that the employee is notified.*
**Acceptance Criteria:** 
1. *When 'Deny' is clicked, a mandatory text box must appear asking for the reason.*
2. *The system must send an automated email via SendGrid to the employee within 5 seconds.*
3. *The requested dates must automatically be removed from the manager's Google Calendar via the Google Calendar API.*

## The Ultimate ROI
Many companies try to save money by cutting the Business Analyst from the offshore contract, assuming the developers can just figure it out. 

This is the most expensive mistake you can make. Developers are highly logical; they will build exactly what you tell them to build. If you give them vague instructions, they will build the wrong thing. By utilizing a skilled Business Analyst, you ensure that every single hour of expensive developer coding time is spent building the exact feature your business actually needs, on the very first try.
