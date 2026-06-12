# How to Outsource a Legacy System Rewrite (Without Crashing the Business)

**Word Count:** ~600 words
**Target Keywords:** legacy software migration, system rewrite, outsourcing legacy systems

Rewriting a legacy software system is the most dangerous project an IT department can undertake. 

It is incredibly common for a company to spend two years and $2 million trying to rewrite their 15-year-old ERP system, only for the project to fail spectacularly, forcing them to continue using the old, broken software.

Because internal teams are usually too busy keeping the old system alive, companies often look to offshore development agencies to handle the rewrite. If you are outsourcing a legacy rewrite, you must follow the **Strangler Fig Pattern**.

## The Mistake: The "Big Bang" Rewrite
The absolute worst way to rewrite software is the "Big Bang." 
This is when you hire an offshore team and say, "Go into a cave for 18 months and build a perfect, modern clone of our massive software. On January 1st, we will turn off the old system and turn on the new one."

This fails 90% of the time. Why?
Because over the last 15 years, thousands of undocumented, invisible business rules were hard-coded into the old system. The new offshore team doesn't know these rules exist. When you flip the switch on January 1st, the new system crashes, the accounting data is corrupted, and the business stops functioning.

## The Solution: The Strangler Fig Pattern
In nature, a Strangler Fig tree grows by wrapping its roots around an older, existing tree. Slowly, over time, the fig tree replaces the old tree entirely, without the old tree ever falling down.

This is exactly how you must rewrite legacy software. You do not rewrite it all at once; you replace it piece by piece.

### Step 1: Wrap the Legacy Code
You place an API Gateway in front of your old software. All user traffic goes through the gateway, which currently just routes everyone to the old, ugly legacy system.

### Step 2: Build One Microservice
You task your offshore dedicated team with rewriting *one tiny piece* of the application. For example, they rewrite just the "User Profile" page using modern React and Node.js. 

### Step 3: Reroute the Traffic
When the new "User Profile" microservice is heavily tested and ready, you change the rules on the API Gateway. Now, when a user clicks "View Profile," the Gateway routes them to the fast, modern offshore code. If they click "View Billing" (which hasn't been rewritten yet), the Gateway routes them to the old legacy code.
The user doesn't even notice the switch. They just think the profile page suddenly got faster.

### Step 4: Repeat and Strangle
The offshore team repeats this process. Next month, they rewrite the Billing module. The next month, the Inventory module. 
Piece by piece, the new, modern microservices "strangle" the legacy system. Eventually, the old system has zero traffic being routed to it, and you simply unplug the server. 

By outsourcing a legacy rewrite using the Strangler Fig pattern, you reduce risk to zero. You deliver continuous, modern value to your users every month, rather than waiting two years for a risky Big Bang launch.
