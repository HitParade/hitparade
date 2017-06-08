import React, { PropTypes, Component } from 'react';

class Modal extends Component {
  static propTypes = {
  	// closeModal: PropTypes.func.isRequired ,
  	// subscribe:  PropTypes.func.isRequired ,
  	isOpen:  PropTypes.bool,
  };

  render () {
    const { isOpen } = this.props;

    return (
      <div className={`modal-overlay ${isOpen ? 'show' : ''}`}>
        <div className="modal-container">
          {this.props.children}
        </div>
      </div>
    )
  }

}

export default Modal;