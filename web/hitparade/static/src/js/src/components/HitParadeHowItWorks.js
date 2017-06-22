import React, { PropTypes } from 'react';
import _ from 'lodash';
import HitParadeHowToPanel from './HitParadeHowToPanel';
import HowItWorksStepsPanel from './HowItWorksStepsPanel';
import siteContent from '../../siteContent.js';

const HitParadeHowItWorks = props => {
  const { header, subHeader, panels } = siteContent.content.howItWorksWhy;
  const { howItWorksSteps } = siteContent.content;
  return (
      <section className="hp-how-it-works">
            <section className="hp-section-how-it-works-container-first">
                  <section className="hp-section-how-h1 niveau-grotesk-black">
                        {header}
                  </section>
                  <section className="hp-why-header-divider">
                        <img 
                              src={siteContent.assets.divider}   
                              className="hp-divider" 
                        />
                  </section>
                  <section className="hp-section-how-ct proxima-nova-regular">
                        {subHeader[0]} 
                        <span className="boldText">
                              &nbsp;
                              {subHeader[1]}
                              &nbsp;
                        </span> 
                        {subHeader[2]} 
                        <span className="boldText">
                              &nbsp;
                              {subHeader[3]}
                              &nbsp;
                        </span> 
                        {subHeader[4]}
                  </section>
                        <section className="hp-section-how-graphics-panel-container">
                        <section className="hp-section-how-graphics-panel">
                        {
                              _.map(panels, (panel) => 
                                    (<HitParadeHowToPanel
                                          key={panel.h1Text}
                                          { ...panel }
                                    />))
                        }
                        </section>
                  </section>
            </section>
            <section className="hp-section-how-it-works-container-second">
            <section className="hp-section-how-h1 niveau-grotesk-black">{howItWorksSteps.header}</section>
            <section className="hp-why-header-divider">
                  <img src={siteContent.assets.divider}  className="hp-divider" />
            </section>
                  <section className="how-it-works-steps-container">
                        {
                              _.map(howItWorksSteps.steps, (panel, i) => 
                                    (<HowItWorksStepsPanel 
                                          key={panel.title}
                                          reverse={i % 2 !== 0}
                                          { ...panel }
                                    />))
                        }
                  </section>
            </section>
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
