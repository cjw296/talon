Concepts
========

What is it?
-----------

Talon is a system for periodically running jobs that have constraints.

A :ref:`job <job>` will be :ref:`run <run>` once per :ref:`period <period>`
once all its :ref:`constraints <constraint>` have been met.

Jobs and any information needed to run them along with their
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
- status
- executor? host?

.. _period:

Period
------

Attributes:

- type
- start
- environment?

Types:

- hourly
- daily
- weekly
- monthly
- querterly

.. _constraint:

Constraint
----------

Types:

- start at
- one other job has completed
- file available
- host of a particular type
- environment?

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
