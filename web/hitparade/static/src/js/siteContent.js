const root = '/static/dist/images';

export default {
    assets: {
        winNumber: `${root}/fiftySix.svg`,
        divider: `${root}/divider.svg`
    },
    content: {
        howItWorksSteps: [
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
    }
}