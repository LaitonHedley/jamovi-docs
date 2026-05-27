import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://docs.jamovi.org',
  integrations: [
    starlight({
      title: 'jamovi Documentation',
      logo: {
        src: './src/assets/header-logo.svg',
      },
      favicon: '/jamovi-v.svg',
      head: [
        {
          tag: 'script',
          attrs: { src: '/gif-player.js', defer: true },
        },
      ],
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
            { slug: 'usermanual/um_6_jamovi_and_R' },
          ],
        },
        {
          label: 'Analyses',
          items: [
            { slug: 'analyses/jg_overview' },
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
            { slug: 'howto/howto_Filtering_data' },
            { slug: 'howto/howto_Install_modules' },
            { slug: 'howto/howto_Use_PROCESS' },
          ],
        },
        {
          label: 'From SPSS to jamovi',
          items: [
            { slug: 'spss2jamovi/s2j_Comparison_of_analyses' },
            { slug: 'spss2jamovi/s2j_side-by-side' },
          ],
        },
      ],
      customCss: ['./src/styles/jamovi.css'],
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/jamovi/jamovi' },
      ],
    }),
  ],
});
