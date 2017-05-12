import React, { PropTypes } from 'react';

const HitParadeHowToPanel = props => {
  return (

            <section className="hp-section-how-graphics-toppanel">
                <div className="hp-svg-icon">
                    <img src={props.imgRoot +props.svg} />
                </div>
                <div className="hp-h1-text niveau-grotesk-black">{props.h1Text}</div>
                <div className="hp-section-how-ct-panel proxima-nova-regular">{props.descText}</div>
            </section>
        );
}
HitParadeHowToPanel.propTypes = {
	svg: PropTypes.string.isRequired,
	h1Text: PropTypes.string.isRequired,
	descText: PropTypes.string.isRequired,
};

export default HitParadeHowToPanel;