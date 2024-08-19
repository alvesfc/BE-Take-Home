# Welcome
Hello 👋<br /><br />
We are thrilled about the possibility of you joining our team. This take-home exercise is designed to help us understand how you approach problems. It's a great opportunity for you to showcase your abilities and for us to see how we might work together.<br /><br />
Thank you for taking the time, and we look forward to speaking with you soon!
### Intro
Finance teams at companies create budgets with some assumptions about their business. Excel is the most widely used tool for this purpose. Here is a simplified example of a budget (financial projections) that you can refer to:<br />
[Financial Projections Example](https://docs.google.com/spreadsheets/d/1B30XbPre5XyD9ItRZ6PN98xCeZe4SplpNQhEjq2ASHo/edit?usp=sharing)<br /><br />
These budgets contain important information about the assumptions the business is making. We are interested in building a feature that parses excel sheets and singles out these assumptions to allow financial decision makers to easily build their budgets in varying business conditions (e.g. what if the Product Sales only go up by 1% per month instead of 4% as provided in the above example)

### Task Description
- Analyze the structure of the sheet provided and sketch out an algorithm that would figuratively read this sheet and synthesize it down into a compact data structure.
- Do not provide a data structure that just saves all the cells as is; this is not the objective. We are primarily interested in your algorithm that parses the relationships between cells or sets of cells that define the budget, synthesizing it to its essentials. 
- Provide a public link to your solution (ideally hosted Github or Google Drive). Format is up to you, but make sure that you explain your thought process in detail.

### Additional Notes
- To help you understand the use case, imagine a scenario where this Excel file is uploaded, and an algorithm has to decipher the relationships between cells or sets of cells so that the projections may be effectively loaded into an application.
- We are not looking for you to build an app or to code; the objective here is to define the approach you will take to build the solution. However, if the problem is pushing you to go all the way, please feel free to go the extra mile. 
- Give it your best shot (don’t let perfect be the enemy of good)
- We encourage you to ask us about anything you're unclear on via email at [careers@finofo.com](mailto:careers@finofo.com)

### Hint
- *Do not* hardcode the rows or columns; you want to have the program itself detect the relationships/formulas. Sheets could come in very varied different formats with different rows, row labels, etc.
