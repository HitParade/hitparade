const root =  '/static/dist/images';

export default {
    url: 'http://hitparade.co',
    assets: {
        winNumber: `${root}/fiftySix.svg`,
        divider: `${root}/divider.svg`,
        facebookF: `${root}/facebook.svg`,
        twitter: `${root}/twitter.svg`,
        closeIcon: `${root}/close.svg`,
    },
    externalLinks: {
        twitterIntentBase: 'https://twitter.com/intent/tweet'
    },
    content: {
        twitterIntent: {
            text: 'Check out HitParade for player performance predictions and trends!',
            url: 'https://hitparade.co'
        },
        howItWorksWhy: {
            header: 'WHY HIT PARADE',
            subHeader: [
                'Use ',
                'Hitparade', 
                'to help shift the odds of ',
                'Beat the Streak', 
                'in your favor!'
            ],
            panels: [
                {
                    imgRoot: root,
                    svg: "/detailedStats.svg",
                    h1Text: "Detailed Statistics",
                    descText: "HitParade visualizes both detailed historical and upcoming game stats to surface the best picks."
                },
                {
                    imgRoot: root,
                    svg: "/predictiveEngine.svg",
                    h1Text: "Predictive Engine",
                    descText: "Hit Parade uses AI to predict player performance in upcoming games."
                },
                {
                    imgRoot: root,
                    svg: "/confidenceLevel.svg",
                    h1Text: "Confidence Level",
                    descText: "We will give you a detailed data visualization and Confidence Level in how likely our prediction is to occur."
                }
            ],
        },
        howItWorksSteps: {
            header: 'HOW IT WORKS',
            steps: [
                {
                    imgSrc: `${root}/howItWorks1.png`,
                    title: "Simple",
                    body: "Data is easy to navigate and understand."
                },
                {
                    imgSrc: `${root}/howItWorks2.png`,
                    title: "Efficient",
                    body: "All information visualized in one place."
                },
                {
                    imgSrc: `${root}/howItWorks3.png`,
                    title: "Advanced",
                    body: "AI Algorithms find hidden value in player performance."
                }
            ]
        },
        share: {
            header: 'share'
        }
    }
}