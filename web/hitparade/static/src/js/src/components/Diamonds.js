import React from 'react'; 
import PropTypes from 'prop-types';
import {times} from 'lodash';

const Diamonds = props => {
    const elements = []
    times(props.count, (i) => {
              elements.push(
                  <div 
                    key={i}
                    className='hp-section-diamond'
                  >
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