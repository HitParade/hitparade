import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

class Test extends Component {
  render() {
    return (
      <div>TESTTTTTT</div>
    );
  }
}

function mapStateToProps(state) {
  return {};
}

function mapDispatchToProps(dispatch) {
  return {} //bindActionCreators(session, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Test);
