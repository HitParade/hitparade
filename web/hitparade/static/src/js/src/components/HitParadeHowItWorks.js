import React, { PropTypes } from 'react';
import HitParadeButton from './HitParadeButton';
import HitParadeHowToPanel from './HitParadeHowToPanel';

const HitParadeHowItWorks = props => {
  return (
            <section className="hp-section-how">
                  <section className="hp-section-how-h1 niveau-grotesk-black">WHY HIT PARADE</section>
                  <section className="hp-why-header-divider">
                        <img src={props.imgRoot+'divider.svg'}   className="hp-divider" />
                  </section>
                  <section className="hp-section-how-ct proxima-nova-regular">
                    Use <span className="boldText">&nbsp;HitParade&nbsp;</span> to help shift the odds of <span className="boldText">&nbsp;Beat the Streak&nbsp;</span> in your favor!
                  </section>
                   <section className="hp-section-how-graphics-panel">
                      <HitParadeHowToPanel
                        imgRoot={props.imgRoot}
                        svg="detailedStats.svg"
                        h1Text="DETAILED STATISTICS"
                        descText="HitParade visualizes both detailed historical and upcoming game stats to surface the best picks." />

                      <HitParadeHowToPanel
                        imgRoot={props.imgRoot}
                        svg="predictiveEngine.svg"
                        h1Text="PREDICTIVE ENGINE"
                        descText="HitParade uses a custom predictive engine to predict if a player will get a hit in an upcoming game." />

                      <HitParadeHowToPanel
                        imgRoot={props.imgRoot}
                        svg="confidenceLevel.svg"
                        h1Text="CONFIDENCE LEVEL"
                        descText="We will give you a detailed data visualization and Confidence Level in how likely our prediction is to occur." />
                   </section>
                   <section className="hp-section-how-h1  niveau-grotesk-black"  style={{marginTop: '40px'}}>HOW IT WORKS</section>
                   <section className="hp-why-header-divider">
                        <img src={props.imgRoot+'divider.svg'}  className="hp-divider" />
                   </section>
                   <div className="hp-panel-row-end">

                        <div className="hp-panel-relative">
                              <div className="hp-img-panel">
                                    <img src={props.imgRoot+'howItWorks1.svg'}  />
                              </div>
                              <div className="hp-panel-text">
                                    <div className="hp-panel-text-h1 niveau-grotesk-black"><img className="hp-diamond-bullet" src={props.imgRoot+'diamondBullet.svg'} /><span className="h1-move">STEP 1:</span></div>
                                    <div className="hp-panel-text-desc proxima-nova-regular">Choose a player from our database.</div>
                              </div>
                        </div>
                       <div className="hp-rectangle"></div>

                  </div>

                   <div className="hp-panel-row-start">

                       <div className="hp-rectangle-ls"></div>
                        <div className="hp-panel-relative">
                              <div className="hp-panel-text">
                                    <div className="hp-panel-text-h1 niveau-grotesk-black"><img className="hp-diamond-bullet" src={props.imgRoot+'diamondBullet.svg'}  /><span className="h1-move">STEP 2:</span></div>
                                    <div className="hp-panel-text-desc proxima-nova-regular">View detailed analytics, stats for all of the chosen players history and view our predictions as to whether the player will get a hit. </div>
                              </div>
                              <div className="hp-img-panel">
                                    <img src={props.imgRoot+'howItWorks2.svg'} />
                              </div>
                        </div>

                  </div>
                  <div className="hp-panel-row-end">


                        <div className="hp-panel-relative">

                              <div className="hp-img-panel">
                                    <img src={props.imgRoot+'howItWorks3.svg'}  />
                              </div>
                              <div className="hp-panel-text">
                                    <div className="hp-panel-text-h1 niveau-grotesk-black"><img className="hp-diamond-bullet" src={props.imgRoot+'diamondBullet.svg'}  /><span className="h1-move">STEP 3:</span></div>
                                    <div className="hp-panel-text-desc proxima-nova-regular">Choose the most probable player(s) to get a hit to Beat the Streak and WIN $5.6 million! </div>
                              </div>
                        </div>
                        <div className="hp-rectangle"></div>
                  </div>
            </section>
        );
}
HitParadeHowItWorks.propTypes = {
	navs: PropTypes.object.isRequired,
};

export default HitParadeHowItWorks;
