// get the ninja-keys element
// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{id: "post-why-trade-deficits-aren-t-bad-and-surpluses-aren-t-always-good",
        
          title: "Why Trade Deficits Aren’t Bad—and Surpluses Aren’t Always Good",
        
        description: "A non-technical discussion of why trade deficits aren’t “losing,” why surpluses aren’t always “winning,” and why the trade balance is often misunderstood.",
        section: "Blogs",
        handler: () => {
          
            window.location.href = "/trade-talk/2025/trade-balance-discussion/";
          
        },
      },{id: "post-asean-trade-balance-interactive-map-2017-2024",
        
          title: "ASEAN Trade Balance: Interactive Map (2017–2024)",
        
        description: "Explore ASEAN’s trade balance with every partner country from 2017–2024 through an interactive, data-driven map.",
        section: "Blogs",
        handler: () => {
          
            window.location.href = "/trade-talk/2025/asean-trade-balance/";
          
        },
      },{id: "post-automating-trade-data-collection-un-comtrade-amp-world-bank-api",
        
          title: "Automating Trade Data Collection: UN Comtrade &amp; World Bank API",
        
        description: "A Python-based automation tool for downloading, merging, and summarizing international trade and macroeconomic data using the official UN Comtrade and World Bank APIs.",
        section: "Blogs",
        handler: () => {
          
            window.location.href = "/trade-talk/2025/trade-research-api/";
          
        },
      },{id: "post-u-s-reciprocal-tariffs-a-cge-analysis-of-global-economic-impacts",
        
          title: "U.S. Reciprocal Tariffs: A CGE Analysis of Global Economic Impacts",
        
        description: "Standard GTAP CGE simulation of the 2025 U.S. reciprocal tariff measures",
        section: "Blogs",
        handler: () => {
          
            window.location.href = "/trade-talk/2025/us-asean-cge-static/";
          
        },
      },{id: "post-u-s-reciprocal-tariff-monitoring-trump-tariffs",
        
          title: "U.S. Reciprocal Tariff Monitoring (Trump Tariffs)",
        
        description: "Interactive visualization of U.S. reciprocal tariff policies implemented in 2025",
        section: "Blogs",
        handler: () => {
          
            window.location.href = "/trade-talk/2025/us-reciprocal-tariff-measures/";
          
        },
      },{id: "news-trump-s-25-tariff-on-canda-and-mexico",
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
          section: "News",},{id: "news-gtapviz-gtap-result-visualization-package-now-officially-on-cran",
          title: 'GTAPViz: GTAP Result Visualization Package Now Officially on CRAN!',
          description: "",
          section: "News",},{id: "news-quantifying-aves-of-ntms-for-cge-model-integration-presentation-at-the-28th-annual-conference-on-global-economic-analysis",
          title: 'Quantifying AVEs of NTMs for CGE Model Integration – Presentation at the 28th...',
          description: "",
          section: "News",},{id: "news-cge-analysis-of-asean-trade-policies-under-u-s-reciprocal-tariffs-presentation-at-the-18th-international-conference-of-economists-kasetsart-university-bangkok-thailand",
          title: 'CGE Analysis of ASEAN Trade Policies under U.S. Reciprocal Tariffs – Presentation at...',
          description: "",
          section: "News",},{id: "news-dynamic-cge-analysis-of-the-u-s-reciprocal-tariff-and-retaliatory-scenarios-presentation-at-the-20th-international-convention-east-asian-economic-association-manila-philippines",
          title: 'Dynamic CGE Analysis of the U.S. Reciprocal Tariff and Retaliatory Scenarios. – Presentation...',
          description: "",
          section: "News",},{id: "news-started-a-short-term-consulting-engagement-with-the-asian-development-bank-adb-as-an-economist-and-resource-person-for-the-project-economic-implications-of-an-asia-wide-free-trade-agreement-evidence-from-gtap-based-cge-simulations",
          title: 'Started a short-term consulting engagement with the Asian Development Bank (ADB) as an...',
          description: "",
          section: "News",},{id: "projects-amata-production-product-catalog-polo",
          title: 'AMATA Production Product Catalog (Polo)',
          description: "Discover AMATA Production&#39;s custom polo shirts — designed for corporate identity, teams, and uniforms. Tailored to your brand with premium fabrics, clean embroidery, and modern sublimation printing. Fast production and factory-direct value.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/AMATAPoloCatalog/";
            },},{id: "projects-amata-production-co-ltd-thailand",
          title: 'AMATA Production Co., Ltd., Thailand',
          description: "AMATA Production Co., Ltd., a business specializing in high-quality apparel, printing solutions, and smart business tools with precision and innovation.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/AMATAProduction/";
            },},{id: "projects-amata-production-product-catalog-sports",
          title: 'AMATA Production Product Catalog (Sports)',
          description: "Explore our sportswear collection from AMATA Production — custom-designed sublimation shirts for teams, events, and organizations. Factory-direct pricing, modern styles, and fast turnaround with top-tier print quality.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/AMATASportsCatalog/";
            },},{id: "projects-bluroca-co-ltd-thailand",
          title: 'Bluroca Co., Ltd., Thailand',
          description: "Bluroca Co., Ltd., a business consulting and execution partner helping Thai manufacturers achieve scalable market growth through data-driven strategy.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Bluroca/";
            },},{id: "projects-gtapviz-gtap-guide",
          title: 'GTAPViz–GTAP Guide',
          description: "A comprehensive guide with sample code to help you process CGE results and generate visualizations with a single click.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/GTAPViz-GTAP-User/";
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
            },},{id: "projects-thai-english-business-nlp",
          title: 'Thai-English Business-NLP',
          description: "Automated Thai–English keyword extraction and sentiment analysis from business-related PDF reports.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Thai_Business_NLP/";
            },},{id: "projects-u-s-reciprocal-tariff-measures-2025",
          title: 'U.S. Reciprocal Tariff Measures (2025)',
          description: "An interactive visualization of Trump’s 2025 reciprocal tariffs and U.S. trade shares using global descriptive trade data.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/USReciprocalTariffVisual/";
            },},{id: "projects-cge-u-s-trade-war",
          title: 'CGE: U.S. Trade War',
          description: "Using GTAP CGE to analyze Trump’s 2025 reciprocal tariffs on global and country economy, illustrating with interactive visualization.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/USTariffCGE_1/";
            },},{id: "worst-moments-best-memories-worst-moments-best-memories",
          title: 'Worst Moments, Best Memories',
          description: "",
          section: "Worst-moments-best-memories",handler: () => {
              window.location.href = "/worst-moments-best-memories/chapter1/";
            },},{id: "worst-moments-best-memories-worst-moments-best-memories",
          title: 'Worst Moments, Best Memories',
          description: "",
          section: "Worst-moments-best-memories",handler: () => {
              window.location.href = "/worst-moments-best-memories/chapter9/";
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
        id: 'social-amata',
        title: 'Amata',
        section: 'Socials',
        handler: () => {
          window.open("https://bodysbobb.github.io/projects/AMATAProduction/", "_blank");
        },
      },];