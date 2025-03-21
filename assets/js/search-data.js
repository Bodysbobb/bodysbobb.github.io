// Set to true to exclude main navigation items// Set to true to exclude dropdown menu items// Set to false to include blog posts in search// Set to false to include books collection in search// Set to false to include theme options in search// Set to true to exclude social media links

// get the ninja-keys element
// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{id: "news-trump-s-25-tariff-on-canda-and-mexico",
          title: 'Trump’s 25% Tariff on Canda and Mexico',
          description: "",
          section: "News",},{id: "news-gtapviz-r-package-for-gtap-result-visualization-in-development",
          title: 'GTAPViz R Package for GTAP Result Visualization: In Development',
          description: "",
          section: "News",},{id: "news-successfully-completed-the-gtap-dynamic-short-course-3-month-program",
          title: 'Successfully completed the GTAP Dynamic Short Course (3-month program).',
          description: "",
          section: "News",},{id: "news-harplus-r-package-for-har-and-sl4-data-extraction-available-on-cran",
          title: 'HARplus R Package for ‘har’ and ‘sl4’ data extraction: Available on CRAN',
          description: "",
          section: "News",},{id: "projects-amata-production-co-ltd-thailand",
          title: 'AMATA Production Co., Ltd., Thailand',
          description: "Co-founder of AMATA Production Co., Ltd., a business specializing in high-quality apparel, printing solutions, and smart business tools with precision and innovation.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/AMATAProduction/";
            },},{id: "projects-gtapviz-r-package",
          title: 'GTAPViz: R Package',
          description: "Facilitates the reporting of CGE model outputs, particularly for GTAP users, but it can also be applied to other results based on &#39;har&#39; and &#39;sl4&#39; file.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/GTAPViz/";
            },},{id: "projects-harplus-r-package",
          title: 'HARplus: R Package',
          description: "Officially available on CRAN, HARplus enhances GEMPACK users&#39; experience by streamlining &#39;har&#39; and &#39;sl4&#39; file processing for multiple inputs simultaneously.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/HARplus/";
            },},{
        id: 'social-email',
        title: 'Email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%70%70%75%61%6E%67%63%68@%70%75%72%64%75%65.%65%64%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/bodysbobb", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/pattawee-puangchit", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=_PHCgeIAAAAJ", "_blank");
        },
      },{
        id: 'social-work',
        title: 'Work',
        section: 'Socials',
        handler: () => {
          window.open("https://gtap.agecon.purdue.edu/network/member_display.asp?UserID=37552", "_blank");
        },
      },{
        id: 'social-custom_social',
        title: 'Custom_social',
        section: 'Socials',
        handler: () => {
          window.open("https://bodysbobb.github.io/projects/AMATAProduction/", "_blank");
        },
      },];