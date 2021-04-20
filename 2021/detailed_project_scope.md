# Project Scope
This document builds on the project scope outlined in our
[project proposal](https://github.com/arviz-devs/arviz/wiki/Season-of-Docs-2021#projects-scope)
to give more details about the project, propose some extra ideas to help with your specific
proposals and provide some insight on our priorities.

## Key milestones

* Evaluate current documentation flow and organization
   * This should happen in light of a documentation framework.
     We have recently done some changes to our documentation following very loosely
     [diataxis](https://diataxis.fr) and
     [thegooddocsproject](https://thegooddocsproject.dev/about/), which we listed as examples in the
     original proposal, but you are not restricted to these two only. You can propose another
     documentation framework you are familiar with.
   * This should take into account the different ArviZ users and different expertise levels on ArviZ
     usage to understand their paths to relevant information
   * This should also take into account the difference between the ArviZ documentation and the
     "Exploratory Analysis of Bayesian Models" (EABM) educational resource. As Osvaldo commented on gitter,
     ArvZ docs are about "how to use ArviZ" whereas EABM is about "how to understand results from ArviZ's"
   * This should also consider readability ensuring the language is accessible by folks from any background,
     ArviZ is used at all formation levels, from students to professors and for people in many
     fields, from particle physics or psychology to economy or molecular biology.
* Write down the results of the evaluation (see below in both key and secondary milestones form more
  details)
   * In "How to write/read ArviZ docs" guides
   * In issues as actionable changes so the whole community can get involved and improve the docs
   * Edit one/a few pages as an example of best practices
* Write a "how to write ArviZ documentation" guide
   * Bring the documentation framework of your choice to ArviZ, explain where each of the parts/blocks
     of the framework are found in ArviZ docs, where should each type of content go, what to do when
     a new function is added, what to do when a new module is added...
* Write "how to read ArviZ docs"/"what to expect" page
   * It should explain where is what, what will users find in getting started pages vs user guide pages vs reference pages,
     what will they find in ArviZ docs and what is in EABM instead...
* A priority list of what the remaining actions are at the end of the projects so we can create issue tickets and continue with the work as a community


## Secondary milestones
* Update documentation based on recommendations
* A writeup on where we started, what happened during the GSOD process, and next actions
* A survey about our users and how they use and want to use docs, an example from scipy is [here](https://github.com/mkg33/GSoD/blob/master/user_survey_summary.pdf)
* Include assessment of sister open source docs from the perspective of an ArviZ user such as xarray and matplotlib as these OSS libraries are crucial for use
* Provide feedback on visual design of graphics

## Out of scope milestones
* Extensive technical explanation of mathematical concepts. E.g. we’re not proving theorems or rewriting papers
* Long form tutorials. We’re not writing a book or case studies
* Updating all the documentation to match the standard set in the report
