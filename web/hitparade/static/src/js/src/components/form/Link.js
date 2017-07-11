import React from 'react'; 
import PropTypes from 'prop-types';
import { Link } from 'react-router';

const LinkInternal = props => {
  const { text } = props;
    return (
      <Link {...props}>
        {text}
      </Link>
    );
}

LinkInternal.propTypes = {
    src: PropTypes.string,
    text: PropTypes.string,
    children: PropTypes.any,
};

export default LinkInternal;