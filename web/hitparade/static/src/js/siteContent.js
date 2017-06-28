const root =  '/static/dist/images';

export default {
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
                    descText: "HitParade uses a custom predictive engine to predict if a player will get a hit in an upcoming game."
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
                    title: "STEP 1:",
                    body: "Choose a player from our database."
                },
                {
                    imgSrc: `${root}/howItWorks2.png`,
                    title: "STEP 2:",
                    body: "View detailed analytics, stats for all of the chosen players history and view our predictions as to whether the player will get a hit."
                },
                {
                    imgSrc: `${root}/howItWorks3.png`,
                    title: "STEP 3:",
                    body: "Choose the most probable player(s) to get a hit to Beat the Streak and WIN $5.6 million!"
                }
            ]
        },
        share: {
            header: 'share'
        }
    }
}