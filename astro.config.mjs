import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://docs.jamovi.org',
  integrations: [
    starlight({
      title: 'jamovi Documentation',
      logo: {
        src: './src/assets/header-logo.svg',
        replacesTitle: true,
      },
      favicon: '/jamovi-v.svg',
      defaultLocale: 'root',
      locales: {
        root:  { label: 'English',      lang: 'en' },
        ar:    { label: 'العربية',      lang: 'ar' },
        da:    { label: 'Dansk',        lang: 'da' },
        de:    { label: 'Deutsch',      lang: 'de' },
        es:    { label: 'Español',      lang: 'es' },
        fi:    { label: 'Suomi',        lang: 'fi' },
        fr:    { label: 'Français',     lang: 'fr' },
        hr:    { label: 'Hrvatski',     lang: 'hr' },
        is:    { label: 'Íslenska',     lang: 'is' },
        it:    { label: 'Italiano',     lang: 'it' },
        ja:    { label: '日本語',        lang: 'ja' },
        ko:    { label: '한국어',        lang: 'ko' },
        nb:    { label: 'Norsk bokmål', lang: 'nb' },
        nn:    { label: 'Norsk nynorsk',lang: 'nn' },
        pl:    { label: 'Polski',       lang: 'pl' },
        pt:    { label: 'Português',    lang: 'pt' },
        ru:    { label: 'Русский',      lang: 'ru' },
        si:    { label: 'සිංහල',        lang: 'si' },
        sl:    { label: 'Slovenščina',  lang: 'sl' },
        sv:    { label: 'Svenska',      lang: 'sv' },
        ta:    { label: 'தமிழ்',        lang: 'ta' },
        tr:    { label: 'Türkçe',       lang: 'tr' },
        uk:    { label: 'Українська',   lang: 'uk' },
        vi:    { label: 'Tiếng Việt',   lang: 'vi' },
        zh_CN: { label: '简体中文',      lang: 'zh-CN' },
        zh_TW: { label: '繁體中文',      lang: 'zh-TW' },
      },
      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { slug: 'usermanual/um_1_installation' },
            { slug: 'usermanual/um_2_first-steps' },
            { slug: 'usermanual/um_3_analyses' },
            { slug: 'usermanual/um_4_spreadsheet' },
            { slug: 'usermanual/um_5_updating_data' },
            { slug: 'usermanual/um_6_jamovi_and_r' },
          ],
        },
        {
          label: 'Analyses',
          items: [
            { slug: 'analyses/jg_overview' },
            { slug: 'analyses/jg_11_descriptive-analyses' },
            {
              label: 't-tests',
              collapsed: true,
              items: [
                { slug: 'analyses/jg_21_t-test-independent' },
                { slug: 'analyses/jg_22_t-test-paired' },
                { slug: 'analyses/jg_23_t-test-onesample' },
              ],
            },
            {
              label: 'ANOVA',
              collapsed: true,
              items: [
                { slug: 'analyses/jg_31_unianova' },
                { slug: 'analyses/jg_32_anova-factorial' },
                { slug: 'analyses/jg_33_anova-rm' },
                { slug: 'analyses/jg_34_anova-mixed' },
              ],
            },
            {
              label: 'Regression',
              collapsed: true,
              items: [
                { slug: 'analyses/jg_52_correlations' },
                { slug: 'analyses/jg_42_regression-linear' },
                { slug: 'analyses/jg_43_regression-logistic' },
              ],
            },
            {
              label: 'Frequency Tests',
              collapsed: true,
              items: [
                { slug: 'analyses/jg_56_frequencies-goodness-of-fit' },
                { slug: 'analyses/jg_51_frequencies-chi-square' },
                { slug: 'analyses/jg_58_frequencies-binomial' },
              ],
            },
            {
              label: 'Factor Analysis',
              collapsed: true,
              items: [
                { slug: 'analyses/jg_53_factor-analysis-efa-cfa' },
                { slug: 'analyses/jg_57_factor-analysis-cfa' },
                { slug: 'analyses/jg_54_reliability', label: 'Reliability Analysis' },
              ],
            },
          ],
        },
        {
          label: 'Data Handling',
          items: [
            { slug: 'data/data_overview' },
            { slug: 'data/data_1_overview_data_variables' },
            { slug: 'data/data_2_computed_variables' },
            { slug: 'data/data_3_transformed_variables' },
            { slug: 'data/data_6_filtering_data' },
            { slug: 'data/data_4_row_v_functions' },
            { slug: 'data/data_5_list_of_functions' },
            { slug: 'data/data_7_restructure_data' },
            { slug: 'data/data_8_common_data_recipes' },
            { slug: 'data/data_9_date_handling' },
          ],
        },
        {
          label: 'How to…',
          items: [
            { slug: 'howto/howto_overview' },
            { slug: 'howto/howto_filtering_data' },
            { slug: 'howto/howto_install_modules' },
            { slug: 'howto/howto_use_process' },
          ],
        },
        {
          label: 'From SPSS to jamovi',
          items: [
            { slug: 'spss2jamovi/s2j_comparison_of_analyses' },
            {
              label: 'Side-by-Side Comparison',
              collapsed: true,
              items: [
                { slug: 'spss2jamovi/s2j_side-by-side' },
                {
                  label: 't-tests',
                  collapsed: true,
                  items: [
                    { slug: 'spss2jamovi/s2j_ttestis' },
                    { slug: 'spss2jamovi/s2j_ttestps' },
                    { slug: 'spss2jamovi/s2j_ttestps2' },
                  ],
                },
                {
                  label: 'ANCOVA',
                  collapsed: true,
                  items: [
                    { slug: 'spss2jamovi/s2j_ancova' },
                    { slug: 'spss2jamovi/s2j_ancova2' },
                    { slug: 'spss2jamovi/s2j_ancova3' },
                    { slug: 'spss2jamovi/s2j_ancova4' },
                    { slug: 'spss2jamovi/s2j_ancova5' },
                  ],
                },
                {
                  label: 'Correlation',
                  collapsed: true,
                  items: [
                    { slug: 'spss2jamovi/s2j_correlation' },
                    { slug: 'spss2jamovi/s2j_correlation2' },
                    { slug: 'spss2jamovi/s2j_correlation3' },
                    { slug: 'spss2jamovi/s2j_correlation4' },
                    { slug: 'spss2jamovi/s2j_correlation5' },
                  ],
                },
                {
                  label: 'Linear Regression',
                  collapsed: true,
                  items: [
                    { slug: 'spss2jamovi/s2j_linreg' },
                    { slug: 'spss2jamovi/s2j_linreg2' },
                  ],
                },
                { slug: 'spss2jamovi/s2j_logreg' },
                {
                  label: 'Non-parametric',
                  collapsed: true,
                  items: [
                    { slug: 'spss2jamovi/s2j_nonparametric' },
                    { slug: 'spss2jamovi/s2j_nonparametric2' },
                    { slug: 'spss2jamovi/s2j_nonparametric3' },
                  ],
                },
                {
                  label: 'Frequencies',
                  collapsed: true,
                  items: [
                    { slug: 'spss2jamovi/s2j_frequencies' },
                    { slug: 'spss2jamovi/s2j_frequencies2' },
                  ],
                },
              ],
            },
          ],
        },
      ],
      components: {
        SiteTitle: './src/components/SiteTitle.astro',
        Banner: './src/components/TranslationNotice.astro',
      },
      customCss: ['./src/styles/jamovi.css'],
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/jamovi/jamovi' },
      ],
    }),
  ],
});
