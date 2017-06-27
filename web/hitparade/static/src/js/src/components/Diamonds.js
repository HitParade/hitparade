import React, { PropTypes } from 'react';
import _ from 'lodash';

const Diamonds = props => {
    const elements = []
    _.times(props.count, () => {
              elements.push(
                  <div className='hp-section-diamond'>
                    <img src={props.src} className="hp-section-why-header-diamond" />
                  </div>
                )
              }
            )
  return (
      <div className={props.className || ''}>
          {elements}
      </div>
  );
}

Diamonds.propTypes = {
	count: PropTypes.number.isRequired,
	src: PropTypes.string.isRequired,
  className: PropTypes.string
};

export default Diamonds;