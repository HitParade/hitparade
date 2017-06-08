import React, { PropTypes, Component } from 'react';

class Modal extends Component {
  static propTypes = {
  	closeModal: PropTypes.func.isRequired ,
  	isOpen:  PropTypes.bool,
  };

  render () {
    const { isOpen, closeModal } = this.props;

    return (
      <div className={`modal-container ${isOpen ? 'show' : ''}`}>
        <div 
          className='modal-overlay'
          onClick={() => closeModal()}
        ></div>
        <div className="modal-content-container">
          {this.props.children}
        </div>
      </div>
    )
  }

}

export default Modal;