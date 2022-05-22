# Evaluation of data visualization effectiveness
ArviZ is a Python and Julia library for exploratory analysis of Bayesian models,
and includes many [vizualizations](https://arviz-devs.github.io/arviz/examples/index.html)
to that end.

As ArviZ developers we strive to follow the literature on effective data visualization,
especially around communicating uncertainty, but there are many factors that make this difficult. Including but not restricted to lack of time to implement or update code, publications that slipped under our radar, unconscious biases towards bad practices.

Therefore, to ensure ArviZ is an active agent in advocating and popularizing
effective data visualization practices we budgeted $2000 as part of our GSoD
2021 application to pay someone external to the team to evaluate the
plots that are available in ArviZ and their defaults.

## Job description
We are expecting a report covering the following points:

* Analysis of available and missing visualizations

  Evaluate which visualizations should be present in ArviZ but are not.
  For each visualization we should get a description of how it would serve ArviZ's goal and some degree of addition priority, not necessarily a ranking, could be
  binning missing visualizations in 3 or 4 high to low priority categories.

* Analysis of current defaults

  Evaluate if ArviZ defaults follow best practices. Write down both things
  we are doing well (if any) and things we need to improve. Any and
  all points related to styling, layout, combination of multiple elements
  can be considered here.

* Analysis of usage advise

  Evaluate current advise included in the ArviZ documentation about
  using each plotting function. As a first approximation this
  should be a list of useful references per plot so users can
  better understand when and how to use each of them.

The report should also consider the opened issues and PRs related to changes in our plotting module
when relevant to each of the three points above.

We emphasize again the need for the report to include rationale for
all comments and references where appropriate. While the report will
be written around ArviZ, it will be published here and we expect
it to be useful to other similar libraries like
[bayesplot](https://mc-stan.org/bayesplot/index.html).

Moreover, it could also act as a seed of a centralized resource
maintained by all Bayesian data viz libraries with advise on
how and when to use each plot, combining them...

## Job requirements
* Not being part of the ArviZ team
* Familiarity with data visualization and uncertainty visualization literature (TODO: any good way
  to evaluate this when getting applications?)
* Familiarity with open source and ability to navigate ArviZ issues and documentation

## Payment
The budget for this project is $2000 which will be paid through NumFOCUS
via [OpenCollective](https://opencollective.com/arviz), wire transfer or PayPal.

Don't hesitate to contact us if you have any doubts about the payment process.

## Contact
For any inquiries about this project, please reach out on [Gitter](https://gitter.im/arviz-devs/season_of_docs).
If a question requires privacy you can also use the email below.

## Applying for the job
Applicants who wish to be hired to write the report should send an email to `arviz.devs@gmail.com`
with the following information:

* CV
* Sample report

  We ask you to choose one of [our plots](https://arviz-devs.github.io/arviz/api/plots.html) and write a sample report for it
  regarding the two last points in the job description.

* Statement of interest

  Short document (between half and a single page) explaining why you are interested in
  writing the report and why do you think we should hire you. Make sure to emphasize how
  you meet the job requirements (described above): publications in data viz, involvement with
  open source projects...
  
* Tentative Work Plan and timeline

  Outline of your planned work. This should include work content and a timeline. 
