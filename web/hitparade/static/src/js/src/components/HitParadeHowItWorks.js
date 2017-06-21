import React, { PropTypes } from 'react';
import _ from 'lodash';
import HitParadeHowToPanel from './HitParadeHowToPanel';
import HowItWorksStepsPanel from './HowItWorksStepsPanel';
import HitParadeFooter from './HitParadeFooter';
import Parallax from 'react-springy-parallax';
import prallaxConfig from '../../parallaxConfig';

const HitParadeHowItWorks = props => {
      const howItWoksSteps = [
            {
                  imgSrc: props.imgRoot + 'howItWorks1.png',
                  title: "STEP 1:",
                  body: "Choose a player from our database."
            },
            {
                  imgSrc: props.imgRoot + 'howItWorks2.png',
                  title: "STEP 2:",
                  body: "View detailed analytics, stats for all of the chosen players history and view our predictions as to whether the player will get a hit."
            },
            {
                  imgSrc: props.imgRoot + 'howItWorks3.png',
                  title: "STEP 3:",
                  body: "Choose the most probable player(s) to get a hit to Beat the Streak and WIN $5.6 million!"
            }
      ]
  return (
                  <section className="hp-how-it-works">
                    <Parallax.Layer
                        offset={prallaxConfig.how.offset}
			      speed={prallaxConfig.how.speed}
							onClick={() => props.parallax}>
                        <section className="hp-section-how-it-works-container-first">
                              <section className="hp-section-how-h1 niveau-grotesk-black">WHY HIT PARADE</section>
                              <section className="hp-why-header-divider">
                                    <img src={props.imgRoot+'divider.svg'}   className="hp-divider" />
                              </section>
                              <section className="hp-section-how-ct proxima-nova-regular">
                                Use <span className="boldText">&nbsp;HitParade&nbsp;</span> to help shift the odds of <span className="boldText">&nbsp;Beat the Streak&nbsp;</span> in your favor!
                              </section>
                                <section className="hp-section-how-graphics-panel-container">
                                   <section className="hp-section-how-graphics-panel">
                                      <HitParadeHowToPanel
                                        imgRoot={props.imgRoot}
                                        svg="detailedStats.svg"
                                        h1Text="Detailed Statistics"
                                        descText="HitParade visualizes both detailed historical and upcoming game stats to surface the best picks." />

                                      <HitParadeHowToPanel
                                        imgRoot={props.imgRoot}
                                        svg="predictiveEngine.svg"
                                        h1Text="Predictive Engine"
                                        descText="HitParade uses a custom predictive engine to predict if a player will get a hit in an upcoming game." />

                                      <HitParadeHowToPanel
                                        imgRoot={props.imgRoot}
                                        svg="confidenceLevel.svg"
                                        h1Text="Confidence Level"
                                        descText="We will give you a detailed data visualization and Confidence Level in how likely our prediction is to occur." />
                                   </section>
                                    </section>
                                </section>

                      </Parallax.Layer>
                    <Parallax.Layer
                            offset={prallaxConfig.how2.offset}
			            speed={prallaxConfig.how2.speed}
							onClick={() => props.parallax}>
                        <section className="hp-section-how-it-works-container-second">
                        <section className="hp-section-how-h1 niveau-grotesk-black">HOW IT WORKS</section>
                        <section className="hp-why-header-divider">
                            <img src={props.imgRoot+'divider.svg'}  className="hp-divider" />
                        </section>
                              <section
                                    className="how-it-works-steps-container"
                              >
                                    {
                                          _.map(howItWoksSteps, (panel, i) => 
                                                (<HowItWorksStepsPanel 
                                                      key={panel.title}
                                                      reverse={i % 2 !== 0}
                                                      { ...panel }
                                                />))
                                    }
                              </section>
                        </section>


                      </Parallax.Layer>
                      <HitParadeFooter playersInCart={props.playersInCart} svgs={props.svgs} navs={props.navigationMethods}  imgRoot={props.imgRoot} />

                    </section>

        );
}
HitParadeHowItWorks.propTypes = {
	navs: PropTypes.object.isRequired,
    playersInCart: PropTypes.number.isRequired,
    imgRoot: PropTypes.string.isRequired,
    svgs: PropTypes.object.isRequired,
    navigationMethods:  PropTypes.object.isRequired,
};

export default HitParadeHowItWorks;
