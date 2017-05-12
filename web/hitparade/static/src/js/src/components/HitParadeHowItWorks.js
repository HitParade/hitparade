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
                        Using Hit Parade to <span className="boldText">&nbsp;Beat The Streak&nbsp;</span> is the same as <span className="boldText">&nbsp;Counting Cards&nbsp;</span> at the Black Jack table!
                  </section>
                  <section className="hp-section-how-ct proxima-nova-regular">
                        Hit Parade helps shift the odds in your favor!
                   </section>
                   <section className="hp-section-how-graphics-panel">
                      <HitParadeHowToPanel
                        imgRoot={props.imgRoot}
                        svg="detailedStats.svg"
                        h1Text="DETAILED STATISTICS"
                        descText="Hit Parade provides both detailed historical and upcoming game statistics in data simple custom data visualization format." />

                      <HitParadeHowToPanel
                        imgRoot={props.imgRoot}
                        svg="predictiveEngine.svg"
                        h1Text="PREDICTIVE ENGINE"
                        descText="Hit Parade uses a custom predictive engine to predict if a player will get a hit in the upcoming game." />

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
                                    <div className="hp-panel-text-desc proxima-nova-regular">Choose the most probable player(s) to get a hit to Beat The Streak and  WIN the $5.6 million! </div>
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
