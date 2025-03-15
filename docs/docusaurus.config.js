/* eslint-disable @typescript-eslint/no-var-requires */
const darkCodeTheme = require('prism-react-renderer/themes/dracula');
const lightCodeTheme = require('prism-react-renderer/themes/github');

// With JSDoc @type annotations, IDEs can provide config autocompletion
/** @type {import('@docusaurus/types').DocusaurusConfig} */
(
  module.exports = {
    title: 'YTauto',
    tagline:
      'Open-Source Framework for AI content automation',
    url: 'https://dev.YTauto.ai',
    baseUrl: '/',
    favicon: 'img/favicon.ico',
    organizationName: 'ArslanHashmmiii',
    projectName: 'YTauto',
    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'throw',
    presets: [
      [
        '@docusaurus/preset-classic',
        /** @type {import('@docusaurus/preset-classic').Options} */
        ({
          docs: {
            path: 'docs',
            sidebarPath: 'sidebars.js',
            editUrl:
              'https://github.com/ArslanHashmmiii/YTauto/edit/stable/docs/',
            versions: {
              current: {
                label: 'current',
              },
            },
            lastVersion: 'current',
            showLastUpdateAuthor: true,
            showLastUpdateTime: true,
          },
          theme: {
            customCss: require.resolve('./src/css/custom.css'),
          },
        }),
      ],
    ],
    plugins: ['tailwind-loader'],
    themeConfig:
      /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
      ({
        
        navbar: {
          hideOnScroll: true,
          logo: {
            alt: 'YTauto',
            src: 'img/logo.png',
          },
          items: [
            // left
            {
              label: 'Docs',
              to: 'docs/how-to-install',
              position: 'right',
            },
            // right
            {
              type: 'docsVersionDropdown',
              position: 'right',
            },
            {
              href: 'https://github.com/ArslanHashmmiii/YTauto',
              position: 'right',
              className: 'header-github-link',
            },
          ],
        },
        colorMode: {
          defaultMode: 'light',
          disableSwitch: false,
          respectPrefersColorScheme: true,
        },
        announcementBar: {
          content:
            '⭐️ If you like YTauto, give it a star on <a target="_blank" rel="noopener noreferrer" href="https://github.com/ArslanHashmmiii/YTauto">GitHub</a>! ⭐️',
        },
        footer: {
          links: [
            {
              title: 'Docs',
              items: [
                {
                  label: 'Getting Started',
                  to: 'docs/how-to-install',
                },

              ],
            },
            {
              title: 'YTauto',
              items: [
                {
                  label: 'Issues',
                  to: 'https://github.com/ArslanHashmmiii/YTauto/issues',
                },
              ],
            },
            {
              title: 'Community',
              items: [
                {
                  label: 'Discord',
                  to: 'https://discord.com/invite/bRTacwYrfX',
                },
              ],
            },
            {
              title: 'Social',
              items: [
                {
                  label: 'GitHub',
                  to: 'https://github.com/ArslanHashmmiii/YTauto',
                },
                {
                  label: 'Twitter',
                  to: 'https://twitter.com/ArslanHashmmiiiHQ',
                },
              ],
            },
          ],
          copyright: `YTauto ${new Date().getFullYear()}`,
        },
        prism: {
          theme: lightCodeTheme,
          darkTheme: darkCodeTheme,
        },
      }),
  }
);
