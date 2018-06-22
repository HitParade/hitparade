import { connect } from 'react-redux';
import React from 'react';
import PropTypes from 'prop-types';

const Main = ({ children }) => (
  <div>
    {/* this will render the child routes */}
    {children}
  </div>
);

Main.propTypes = {
  children: PropTypes.any.isRequired,
};

const mapStateToProps = (/* state */) => ({});


export default connect(mapStateToProps)(Main);
