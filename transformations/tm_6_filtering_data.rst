.. sectionauthor:: Laiton Hedley

.. _filtering-data:

==============
Filtering Data
==============

Use **Filters** to subset your data for specific analyses without deleting any
rows. For example, you can restrict an analysis to only participants who smoke,
or only those within a certain age range.

Adding a Filter
---------------

1. Click the **Data** tab in the ribbon.
2. Click the **Filters** button. A filter row will appear at the top of your
   dataset.
3. Type your criteria into the formula box (e.g., ``Smoke == 'Yes'``).

|Filter_Data|

Once applied, the first column of your spreadsheet shows which rows are
included (✔) and which are excluded (✘). Any analysis or plot you create will
now only use the included rows.

.. list-table:: Example of Filtering Data
   :header-rows: 1

   * - Filter
     - Smoke
     - Outcome
   * - ✔
     - Yes
     - 10
   * - ✘
     - No
     - 4
   * - ✘
     - No
     - 6
   * - ✔
     - Yes
     - 9
   * - ✔
     - Yes
     - 9

Using Complex Criteria
----------------------

You can filter based on multiple variables using the ``and`` and ``or``
operators. For example, to include only female participants aged 30 and over,
use:

``Sex == 'Female' and Age >= 30``

Managing Multiple Filters
-------------------------

You can create multiple independent filters by clicking the plus icon (+) in
the filter editor. Each filter can be toggled on or off using the switch next
to its name. This allows you to quickly compare different subsets of your data.

|Toggle_Filter_Data|

To remove a filter entirely, open the filter editor and click the red **×**
icon next to the filter's name. Toggling a filter off temporarily disables it
without losing the expression — deleting it removes it for good.

.. note::
   **Variable functions** (e.g., ``VMEAN()``, ``VSTDEV()``) cannot be used
   directly inside a filter expression. This is because filters exclude data,
   which would change the very statistic (like the mean) you are trying to
   filter by, creating a "circular" calculation that never ends.

   If you need to filter based on a whole-column statistic (like "only rows
   above the mean"), first create a :doc:`Computed Variable <tm_2_computed_variables>`
   using the V function, then filter based on that new column. This "freezes"
   the statistic so the filter can use it reliably.


.. |Filter_Data| image:: /_images/tr_filter_example.png
   :alt: The filter editor in jamovi with the expression Smoke == 'Yes'.
   :class: centered
   :width: 600px

.. |Toggle_Filter_Data| image:: /_images/tr_toggle_filter.png
   :alt: Two filters in the filter editor, each with an on/off toggle.
   :class: centered
   :width: 600px
