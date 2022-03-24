# Centralized documentation for computational Bayesian workflow

## About ArviZ
ArviZ is an open source project dedicated to building tools for Exploratory Analysis of Bayesian Models.
Statisticians and data analysts, across both academic and industry, across programming languages
and across probabilistic programming frameworks use ArviZ to assist them to perform statistical workflows.
They study a wide range of problems, from the effectiveness of cancer treatments,
to SpaceX rocket supply chains, to user behavior on the internet.

To aid with Bayesian modeling analysis ArviZ provides both numerical and visual summaries,
as well as a collection of software tools that help with modeling and storage of statistical results.

ArviZ currently has a Julia and a Python interface and we are working on compatibility with R too.
To date of writing, ArviZ integrates with at least 9 different Probabilistic Programming Languages (PPLs),
including all major PPLs like Stan, PyMC or Turing.

### Contact
For any inquiry about Season of Docs at ArviZ, contact us at [gitter](https://gitter.im/arviz-devs/season_of_docs).

## Project motivation
Writing educational content to teach how to use ArviZ is hard, writing educational content to teach
how to use PPLs is hard and writing content to teach how to use Bayesian modeling is also hard.
However, the good news is that all these are not inherently hard because of some exceptional
technical complexity. One huge challenge in writing such educational material is that
all these tasks are actually one and the same, a wider task generally called
[Bayesian workflow](https://arxiv.org/abs/2011.01808).

Solving real problems with Bayesian modeling requires computational tools,
so trying to explain Bayesian modeling without using any PPL is very limited.
But at the same time, explaining how to use a PPL to someone who doesn't know
anything about Bayesian modeling is also a fool's errand.
And any modeling without visualization, diagnostics and model checking is
doomed from the start.
**We need to teach all these skills at the same time in an organized and coherent manner**

In fact, this is already what is happening. For several years already,
all books in Bayesian modeling use and explain computational tools,
they very often have a "paired" GitHub repo with the code used in the book,
_and the most popular books are "translated" to other PPLs and programming languages_.
To give one example, [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/)
has had their code examples translated into at least 3 programming languages
(R, Python and Julia) and multiple PPLs. The book homepage lists 10 such translations.
A 2 minute search to see if the book had been translated into Spanish only
brought up Spanish bookstores selling the original English version of the book.

## About the project
Given's ArviZ position within the PPL ecosystem; some of the members of our team
are also members of PPL development teams. We would like to create an open, collaborative, online
and multi-language (in all its meanings!) educational resource about the Bayesian workflow.

The goal of the project is to set up all the infrastructure for such a resource to
avoid duplication, and once this is achieved guide the ArviZ educational lead
so they can start writing content.

## Project’s scope
The Arviz documentation project will
* Evaluate multiple alternatives to generate this Bayesian workflow resource.
  The ideal requirements are:
  - The bulk of the explanation/prose content will be common.
    The _multiple_ pages for each programming language and PPL need to be combined
    with the _single_ explanation source of truth and rendered.
  - The code examples must be written in executable files and store its outputs
    for rendering automatically (and without extra code).
    This will not be a static resource and will need to be reexecuted regularly.
  - The explanation content must be written in a format that supports internationalization.
    Ideally, code annotations or comments would too, but they can be avoided
    or kept in English.
  - Changes to the explanation content should be reflected on the website automatically
    when merged. Reexecuting and updating code outputs can have manual steps.
* Set up all a proof of concept in the [bayesian-workflow](https://github.com/arviz-devs/bayesian-workflow) repo
  together with all CI/CD necessary for updating the content.
* Write documentation about maintaining the repository.
* Define the style and structure of the resource.
* Start adding some example/template pages (together with the ArviZ educational lead).
  For example, a quick way to add content and motivate other people to
  collaborate would be adapting some case studies from the documentations
  of PPLs.

Work that is out of scope for this project
* Writing the actual resource.

### Measuring your project’s success
Given the scope of the enterprise and its very early stage, we believe the best metrics are:
* Publishing the proof of concept (yes/no kind of metric)
* Motivating external collaborators (and keeping ArviZ team member motivated)
  to write content on the website (as opposed to driving them away due to a too cumbersome
  writing workflow for example). Once the proof of concept is working, and potential
  collaborators have seen and tested the process we would like to have 4 committed collaborators
  (excluding the ArviZ technical lead that is a hired position).

We do not think that views are a valuable nor valid metric because it will be a resource
in early stages of construction and won't have been advertised yet by then.

## Project budget

* Technical writer $10,000
* Volunteer stipend for mentor $500
* Buying and 2 year renovation of domain name $50
* Downstream donation to infrastructural dependencies $450
  - Any extra funds left from the domain budget item after buying will be used here.

**Total**: $11,000
