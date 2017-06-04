import React, { PropTypes } from 'react';

import HitParadeLogo from './HitParadeLogo';
import HitParadeLeftMenuItem from './HitParadeLeftMenuItem';
import HitParadeRightMenuItem from './HitParadeRightMenuItem';
import HitParadeButton from './HitParadeButton';
import HitParadeShoppingCart from './HitParadeShoppingCart';

const HitParadeHeader = props => {
  const top_menu = props.isLive === 'true' ? (
     <div className="header-top">
    <div className="hp-left-bar ">
         <HitParadeLeftMenuItem imgRoot={props.imgRoot}  classNames="hp-header-item proxima-nova-regular " menuItemText="Select Players"  clickMethod={props.navs.click.navSelectPlayers} />
         <HitParadeLeftMenuItem imgRoot={props.imgRoot}  classNames="hp-header-item proxima-nova-regular " menuItemText="FAQ"  clickMethod={props.navs.click.navFaq}  />
         <HitParadeLeftMenuItem imgRoot={props.imgRoot}  classNames="hp-header-item proxima-nova-regular " menuItemText="Contact" svg={props.svgs.svgContact} clickMethod={props.navs.click.navContact} />
         <HitParadeLeftMenuItem imgRoot={props.imgRoot}  classNames="hp-header-item proxima-nova-regular " menuItemText="Share"  svg={props.svgs.svgShare} clickMethod={props.navs.click.navShare}  />
       </div>
      <div className="hp-right-bar ">
            <HitParadeShoppingCart imgRoot={props.imgRoot} cartCount={props.playersInCart} svgCart={props.svgs.svgCart} clickMethod={props.navs.click.cart} />
            <HitParadeLeftMenuItem imgRoot={props.imgRoot}  classNames="hp-header-item-right proxima-nova-regular " menuItemText=" Sign Up"  clickMethod={props.navs.click.navSignup}  />
            <HitParadeButton imgRoot={props.imgRoot}  buttonText="Login" className="hp-login-button niveau-grotesk-black" clickMethod={props.navs.click.navLogin}/>

     </div>
     </div>
  ) : (
       <div className="header-top">
    <div className="hp-left-bar ">
            <HitParadeLeftMenuItem imgRoot={props.imgRoot}  classNames="hp-header-item proxima-nova-regular " menuItemText="Share"  svg={props.svgs.svgShare} clickMethod={props.navs.click.navShare}  />
       </div>
      <div className="hp-right-bar ">
           <HitParadeButton imgRoot={props.imgRoot} buttonText="Beta Sign Up" className="hp-signup-button niveau-grotesk-black" clickMethod={props.navs.click.navSignup}/>
     </div>
     </div>
  );
  return (

    <nav className="header">
      <HitParadeLogo imgRoot={props.imgRoot} logoColor="#FFFFFF" className="hp-header-item-logo" logoWidth="126px" logoHeight="43px" logoViewBox="0 0 126 43"/>
      {top_menu}
    </nav>
  );
};

HitParadeHeader.propTypes = {
  svgs: PropTypes.object.isRequired,
  playersInCart: PropTypes.number.isRequired,
  isLive: PropTypes.string.isRequired,
  imgRoot: PropTypes.string,
};

export default HitParadeHeader;
