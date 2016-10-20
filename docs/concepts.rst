Concepts
========

What is it?
-----------

Talon is a system for periodically running jobs that have constraints.

A :ref:`job <job>` will be :ref:`run <run>` when :ref:`triggered <trigger>`,
but will block until all its :ref:`constraints <constraint>` have been met.
Each run will occur in a :ref:`period <period>`.

Jobs and any information needed to run them
are stored in the :ref:`configuration <config>` store.

Periods and runs that occur within them are stored in the :ref:`state <state>`
store.


Anti-goals
----------

Talon does not aim to do any of the following:

- Get software, including itself, to where executors need it.

- Get data used by jobs run by executors to those executors.

- Implementation of executors is not the focus, managing constraints and state
  is the focus.

.. _job:

Job
---

.. _run:

Attributes

- name

Run
---

- job
- period
- started
- finished
- state
- executor

States are one of the following:

- blocked - triggered, but one or more constraints have not been met
- ready - constraints have been met
- running - an executor is executing this run
- succeeded
- failed
- skipped - cancelled by a constraint

The executor indicates who 'owns' the job.

.. _period:

Period
------

Attributes:

- type
- start
- environment?

Types:

- daily
- weekly
- monthly
- querterly

.. _constraint:

Constraint
----------

Types:

- start by
- once other specified job has completed
- not more than one successful run in a period
- not more than one instance can running at once
- not more than one instance can blocked at once

When checked, contraints will return one of the following actions to take:

- block - this constraint has not been met
- fail - this constraint can never be met and the run should be failed
- pass - this constraint has been met.
- cancel - this constraint has indicated that the current run should be skipped

.. _trigger:

Trigger
-------

These create the :ref:`run <run>`.

Examples:

- extended cron-style, eg:
  "every 15 minutes between 7-10am, hourly until 4pm,
  every 5 minutes between 4-5pm"

- external

- prior job run completed

.. _executor:

Executor
--------

Not of interested right now, just use cron to trigger!

.. _config:

Config
------

Stores configuration required to run jobs.

.. _state:

State
-----

Stores information about the runs of jobs.
