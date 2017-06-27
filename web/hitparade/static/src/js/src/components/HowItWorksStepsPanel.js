import React, { PropTypes } from 'react';
import _ from 'lodash';

const HowItWorksStepsPanel = props => {
  return (
      <div className={`steps-panel ${props.reverse ? 'reverse' : ''}`}>
          <div className="steps-panel-rectangle"></div>
          <figure className="steps-panel-image-container">
                <img 
                src={props.imgSrc}
                className="steps-panel-image"
                />
           </figure>
           <div className="steps-panel-text-container">
              <div 
                className="steps-panel-title niveau-grotesk-black"
              >
                { props.title }
             </div>
              <p 
                className="steps-panel-body proxima-nova-regular"
              >
                { props.body }
            </p>
          </div>
      </div>
  );
}

HowItWorksStepsPanel.propTypes = {
	imgSrc: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    body: PropTypes.string.required,
    reverse: PropTypes.bool
};

export default HowItWorksStepsPanel;