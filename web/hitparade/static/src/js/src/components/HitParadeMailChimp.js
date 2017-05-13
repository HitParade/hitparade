import React, { Component, PropTypes }  from 'react';
import HitParadeLogo from './HitParadeLogo';

export default class HitParadeMailChimp  extends Component {
	constructor () {
    super();
    this.state = {
      emailAddress: ''
    };
   }
  static propTypes = {
  	closeModal: PropTypes.func.isRequired ,
  	subscribe:  PropTypes.func.isRequired ,
  };
  state = { emailAddress: '' };
  onNameChange = (e) => {
    const emailAddress = e.target.value;
    this.setState({ emailAddress });
  };
 render() {
	  return (

		  	<div id="mc_embed_signup">
		  	<HitParadeLogo logoColor="#2d2d2d" className="hp-header-item-logo" logoWidth="126px" logoHeight="43px" logoViewBox="0 0 126 43"/>
      			<img src={this.props.imgRoot + 'close.svg'}  className="hp-modal-close" onClick={() => this.props.closeModal()} />

				<form action="//matrixoft.us15.list-manage.com/subscribe/post?u=f083a510f29ff28bf9952fba5&amp;id=956366c29f" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" className="validate" target="_blank" noValidate>
				    <div id="mc_embed_signup_scroll">
				    	<label htmlFor="mce-EMAIL">Subscribe to our mailing list</label>
				    	<input
				    		type="email"
				    		name="EMAIL"
				    		className="email"
				    		id="mce-EMAIL"
				    		required
				            value={this.state.emailAddress}
				            onChange={this.onNameChange}
				            placeholder="Email Address"
				            />
					    <div style={{position: 'absolute', left: '-5000px'}} aria-hidden="true">
					    	<input type="text" name="b_f083a510f29ff28bf9952fba5_956366c29f" tabIndex="-1" value=""/>
					    </div>
					    <div className="clear">
					    	<input type="submit"   value="Subscribe" name="subscribe" id="mc-embedded-subscribe" className="button"/>
					    	</div>
					    </div>
				</form>
			</div>
		);
	}
}