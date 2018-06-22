import React from 'react'; 
import PropTypes from 'prop-types';

const HitParadeShoppingCart = props => {
  if(props.cartCount > 0) {
	  return (
	            <div className="hp-shopping-cart " onClick={() => props.clickMethod()}>
	          		<img src={props.imgRoot + props.svgCart.img} style={{width: props.svgCart.width ,height: props.svgCart.height }} />
	             	<div className="hp-shopping-cart-value"> {props.cartCount}</div>
	            </div>
	        );
  } else {
  	  return (
             <div className="hp-shopping-cart">
	          		<img src={props.svgCart.img} style={{width: props.svgCart.width ,height: props.svgCart.height }} />
	         </div>
        );
  }

}
HitParadeShoppingCart.propTypes = {
	cartCount: PropTypes.number,
	clickMethod: PropTypes.func.isRequired,
};

export default HitParadeShoppingCart;