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
                  imgSrc: props.imgRoot + 'howItWorks1.svg',
                  title: "STEP 1:",
                  body: "Choose a player from our database."
            },
            {
                  imgSrc: props.imgRoot + 'howItWorks2.svg',
                  title: "STEP 2:",
                  body: "View detailed analytics, stats for all of the chosen players history and view our predictions as to whether the player will get a hit."
            },
            {
                  imgSrc: props.imgRoot + 'howItWorks3.svg',
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
                        {/*<div className="hp-panel-row-container">
                        <div 
                              className="hp-panel-row-end"  
                              data-170-center="opacity: 1;transform: translateX( 0% ); "
                              data-200-center="opacity: 1;transform: translateX( 50% );  "
                              data-220-center="opacity: 0.01;transform: translateX( 100% );  "
                        >

                            <div className="hp-panel-relative">
                                  <div className="hp-img-panel">
                                        <img src={props.imgRoot + 'howItWorks1.svg'}  />
                                  </div>
                                  <div className="hp-panel-text">
                                        <div className="hp-panel-text-h1 niveau-grotesk-black"><img className="hp-diamond-bullet" src={props.imgRoot+'diamondBullet.svg'} /><span className="h1-move">STEP 1:</span></div>
                                        <div className="hp-panel-text-desc proxima-nova-regular">Choose a player from our database.</div>
                                  </div>
                            </div>
                           <div className="hp-rectangle"></div>

                      </div>
                        </div>*/}
                       {/*<div className="hp-panel-row-container">
                              <div 
                                    className="hp-panel-row-start"  
                                    data-170-center="opacity: 1;transform: translateX( 0% ); "
                                    data-200-center="opacity: 1;transform: translateX( -50% );  "
                                    data-220-center="opacity: 0.01;transform: translateX( -100% );  "
                              >
                            <div className="hp-panel-relative">
                                  <div className="hp-panel-text">
                                        <div className="hp-panel-text-h1 niveau-grotesk-black"><img className="hp-diamond-bullet" src={props.imgRoot+'diamondBullet.svg'}  /><span className="h1-move">STEP 2:</span></div>
                                        <div className="hp-panel-text-desc proxima-nova-regular">View detailed analytics, stats for all of the chosen players history and view our predictions as to whether the player will get a hit. </div>
                                  </div>
                                  <div className="hp-img-panel">
                                        <img src={props.imgRoot + 'howItWorks2.svg'} />
                                  </div>
                            </div>
                            <div className="hp-rectangle-ls"></div>
                      </div>
                       </div>*/}
                      {/*<div className="hp-panel-row-container">
                      <div 
                        className="hp-panel-row-end" 
                        style={{marginBottom: '250px'}}  
                        data-170-center="opacity: 1;transform: translateX( 0% ); "
                        data-200-center="opacity: 1;transform: translateX( 50% );  "
                        data-220-center="opacity: 0.01;transform: translateX( 100% );  "
                        >


                            <div className="hp-panel-relative">

                                  <div className="hp-img-panel">
                                        <img src={props.imgRoot + 'howItWorks3.svg'}  />
                                  </div>
                                  <div className="hp-panel-text">
                                        <div className="hp-panel-text-h1 niveau-grotesk-black"><img className="hp-diamond-bullet" src={props.imgRoot+'diamondBullet.svg'}  /><span className="h1-move">STEP 3:</span></div>
                                        <div className="hp-panel-text-desc proxima-nova-regular">Choose the most probable player(s) to get a hit to Beat the Streak and WIN $5.6 million! </div>
                                  </div>
                            </div>
                            <div className="hp-rectangle"></div>
                      </div>
                      </div>*/}
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
