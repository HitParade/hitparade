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
      <div className={`modal-container ${isOpen ? 'show' : ''}`}>
        <div className='modal-overlay'></div>
        <div className="modal-content-container">
          {this.props.children}
        </div>
      </div>
    )
  }

}

export default Modal;