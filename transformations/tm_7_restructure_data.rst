.. sectionauthor:: Laiton Hedley

.. _restructure-data:

==================
Restructuring Data
==================

What is Wide vs Long Format?
-----------------------------

Within data analysis, two common data structures are *wide format* and
*long format*.

In wide format, each row represents a participant and repeated measurements
are stored in separate columns (one column per outcome at each time point or
condition). For example, below are quiz scores for students during Weeks 2, 4,
and 6 of a semester displayed in wide format:

.. list-table:: Wide Format Example
   :header-rows: 1

   * - ID
     - ScoreWeek_2
     - ScoreWeek_4
     - ScoreWeek_6
   * - 1
     - 30
     - 50
     - 70
   * - 2
     - 20
     - 30
     - 55
   * - 3
     - 40
     - 50
     - 52

Each row represents a unique student (ID), and their quiz scores at Weeks 2, 4,
and 6 are stored in separate columns. To run a repeated measures ANOVA in
jamovi, the data must be in wide format as shown above.

In long format, each row represents a single measurement occasion, giving
multiple rows per participant. The same data in long format:

.. list-table:: Long Format Example
   :header-rows: 1

   * - ID
     - Time
     - Score
   * - 1
     - Week_2
     - 30
   * - 1
     - Week_4
     - 50
   * - 1
     - Week_6
     - 70
   * - 2
     - Week_2
     - 20
   * - 2
     - Week_4
     - 30
   * - 2
     - Week_6
     - 55
   * - 3
     - Week_2
     - 40
   * - 3
     - Week_4
     - 50
   * - 3
     - Week_6
     - 52

Long format makes it easy to summarise, plot, and model change over time
because time is represented explicitly as data rather than being embedded in
column names. It is also required for mixed modelling.

Restructuring with jReshape
---------------------------

.. important::
   Restructuring data in jamovi requires the **jReshape** module, which is not
   installed by default. Install it by clicking the ``+`` icon in the top-right
   of jamovi and searching for ``jReshape``.

Once installed, a ``Data`` option will appear under the ``Analyses`` tab,
containing the jReshape options.

Wide to Long
~~~~~~~~~~~~

1. Click the **Analyses** tab, select **Data**, then select **Wide to Long**.
2. Move the columns that represent repeated measurements (e.g. ``ScoreWeek_2``,
   ``ScoreWeek_4``, ``ScoreWeek_6``) into the **Columns to row** box.
3. Under **Target Variable**, give the new column a meaningful name (e.g. ``Score``).
4. Under **Index Variable**, name the variable that will identify the time point
   or condition (e.g. ``Time``).
5. Check the data preview in the output window. If it looks correct, click
   **Create** and jamovi will open a new window with the restructured data.

Long to Wide
~~~~~~~~~~~~

1. Click the **Analyses** tab, select **Data**, then select **Long to Wide**.
2. Move the outcome variable (e.g. ``Score``) into the **Rows to Columns** box.
3. Move the variable identifying each time point or condition (e.g. ``Time``)
   into the **Indexing Variables** box.
4. Move the participant identifier (e.g. ``ID``) into the **ID Variable** box.
5. Check the data preview, then click **Create**.
