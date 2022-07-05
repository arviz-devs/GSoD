# Centralized documentation for computational Bayesian workflow

## About ArviZ
ArviZ is an open-source library dedicated to building tools for Exploratory Analysis of Bayesian Models. 
Statisticians and data analysts across both academic and industry, across programming languages 
and across probabilistic programming frameworks trust ArviZ to assist them to perform statistical workflows. 
They study a wide range of problems, from the effectiveness of cancer treatments 
to SpaceX rocket supply chains and even user behaviour on the internet.

To aid with Bayesian modeling analysis, ArviZ provides both numerical and visual summaries,
as well as a collection of software tools that help with modeling and storing statistical results.

ArviZ currently has a Julia and a Python interface and we are working on compatibility with R too.
To date of writing, ArviZ integrates with at least 9 different Probabilistic Programming Languages (PPLs),
including all major PPLs like Stan, PyMC or Turing.

### Contact 
For any inquiry about Season of Docs at ArviZ, contact us at gitter.

## Project motivation
Writing educational contents to teach how to use ArviZ  could pose a certain level of difficulty, producing educational contents to teach
how to use PPLs and Bayesian modeling could equally pose a level of difficulty. This difficulty isn't because these frameworks and libraries are inherently complex or too technical but rather as a result of having an encompassing documentation that captures all
the possible libraries that are used with the Bayesian workflow
without doing a disservice to any group of users by not capturing their choice of library or language. 
Here's the icebreaker, writing such educational material/guide is actually one and the same, 
a wider task generally called Bayesian workflow.[Bayesian workflow](https://arxiv.org/abs/2011.01808].

Solving real problems with the Bayesian model requires computational tools, 
so trying to explain Bayesian modeling without using any PPL is very limited and not efficient. 
But at the same time, explaining how to use a PPL to someone who doesn't know 
anything about Bayesian modeling is also a fool's errand. 
Any modeling without visualization, diagnostics and model checking is 
doomed from the start.
**We need to teach all these skills at the same time in an organized and coherent manner**.

In fact, this is already what is happening. For several years now, 
all books in Bayesian modeling uses and explain computational tools, 
they very often have a "paired" GitHub repo with the code used in the book, 
_and the most popular books are "translated" to other PPLs and programming languages._ 
To give one example, [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/)
has had their code examples translated into at least 3 programming languages 
(R, Python and Julia) and multiple PPLs. The book homepage lists 10 such translations. 
A 2 minute search to see if the book had been translated into Spanish only 
brought up Spanish bookstores selling the original English version of the book.

## About the project
Given ArviZ's position within the PPL ecosystem, some of the members of our team 
double as members of PPL development teams. We would like to create an open, collaborative, online 
and multi-language (in all its meanings!) educational resource about the Bayesian workflow. This resource will cover the various compatible libraries that can be used to create Bayesian workflow with sample visualizations and codes.

The goal of the project is to set up all the infrastructure for such a resource to 
avoid duplications like the one encountered above, and once this is achieved, guide the ArviZ educational lead 
so they can start writing content.

### Project’s scope
The Arviz documentation project scope includes the following:
* Evaluate multiple alternatives to generate this Bayesian workflow resource. 
  The ideal requirements are:
- The bulk of the explanation/prose content will be common. 
  The _multiple_ pages for each programming language and PPL need to be combined 
  with the single explanation source of truth and rendered.
- The code examples must be written in executable files and store their outputs
  for rendering automatically (and without extra code). 
  This will not be a static resource and will need to be updated regularly.
- The explanation content must be written in a format that supports internationalization. 
  Ideally, code annotations or comments would do but they can be avoided or kept in English.

- Changes to the explanation content should be reflected on the website automatically
  when merged. Reexecuting and updating code outputs can have manual steps.
* Set up  a proof of concept in the [bayesian-workflow](https://github.com/arviz-devs/bayesian-workflow) repo
* together with all CI/CD necessary for updating the content.
* Regular presentations to the ArviZ team about the writing workflow.
* Write documentation about maintaining the repository.
* Define the style and structure of the resource.
* Start adding some example/template pages (together with the ArviZ educational lead). 
* For example, a quick way to add content and motivate other people to 
* collaborate would be to adopt some case studies from the documentation 
* of PPLs.

  Work that is out of scope for this project
* Writing the actual resource.

### Measuring your project’s success
Given the scope of the enterprise and its very early stage, we believe the best metrics are:
* Publishing the proof of concept (yes/no kind of metric)
* Guiding ~3 ArviZ team members or external collaborators through the process of adding new pages and translations, 
  so they can continue working independently.
- We tried setting up some different educational resources a few years ago, but 
  the writing workflow was very complicated, most of us were unable to 
  generate previews and they were not automated either. Even if it is an 
  unconventional metric, we believe it is key for the project's success 
  that we, as the ones who will write and onboard external collaborators, 
  understand the writing process and feel comfortable with it.

 We do not think that views are a valuable nor valid metric because it will be a resource in 
 early stages of construction and won't have been advertised by then.

## Project budget

Budget item

* Technical writer to create, update and review documentation of the infrastructure.
$10,000
* Volunteer stipend for mentor $500.
 $500
* Domain registration and renovation.
$50
* Downstream donation to infrastructural dependencies like sphinx to generate the website from the source docs, libraries like myst-nb to parse the jupyter notebooks as  sources for the website, readthedocs for building and hosting the website+translations, transifex for managing collaborative translations. 
 $450
 
* Donations
 Any extra funds left from the domain budget item will be used here.


**TOTAL** : $11,000.

