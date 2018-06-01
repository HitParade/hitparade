import React, { PropTypes } from 'react';

import HitParadeLogo from './HitParadeLogo';
import HitParadeLeftMenuItem from './HitParadeLeftMenuItem';
import HitParadeButton from './HitParadeButton';

const HitParadeFooter = props => {
  var d = new Date();
  var fullYear = d.getFullYear();
  return (
    <footer className="footer" style={{
    display: 'flex',
    flexDirection: 'column',
    padding: '15px',
    justifyContent: 'center',
    alignItems: 'center'
}}>
    <div className="site-content-max-width footer-content">
      <img src="/static/dist/images/real-time-stats-provided-by-sportradar-reversed-300w.png" />
    </div>
      <div className="site-content-max-width footer-content">
        <HitParadeLogo logoColor="#FFFFFF" className="hp-footer-logo-ph" logoWidth="126px" logoHeight="43px" logoViewBox="0 0 126 43"/>
        <div className="hp-footer-menu">
          <div className="hp-footer-menu-bar-desktop   hp-remove">
              <div className="hp-left-bar hp-remove">
                  <HitParadeLeftMenuItem imgRoot={props.imgRoot} classNames="hp-header-item proxima-nova-regular" menuItemText="Select Players"  clickMethod={props.navs.click.navSelectPlayers} />
                <HitParadeLeftMenuItem  imgRoot={props.imgRoot} classNames="hp-header-item proxima-nova-regular" menuItemText="FAQ"  clickMethod={props.navs.click.navFaq}  />
                <HitParadeLeftMenuItem  imgRoot={props.imgRoot} classNames="hp-header-item proxima-nova-regular" menuItemText="Contact" svg={props.svgs.svgContact} clickMethod={props.navs.click.navContact} />
                <HitParadeLeftMenuItem  imgRoot={props.imgRoot} classNames="hp-header-item proxima-nova-regular" menuItemText="Share"  svg={props.svgs.svgShare} clickMethod={props.navs.click.navShare}  />
                <HitParadeLeftMenuItem  imgRoot={props.imgRoot} classNames="hp-header-item proxima-nova-regular" menuItemText="Terms of Use"   clickMethod={props.navs.click.navTermsOfUse}  />
              </div>
              <div className="hp-right-bar  hp-remove">
                          <HitParadeLeftMenuItem imgRoot={props.imgRoot} menuItemText="Sign Up"  clickMethod={props.navs.click.navSignup}  />
                          <HitParadeButton buttonText="Login" className="hp-login-button-footer niveau-grotesk-black" clickMethod={props.navs.click.navLogin}/>

              </div>
                <div className="hp-left-bar"></div>
                <div className="hp-right-bar">
                      <HitParadeButton buttonText="Beta Sign Up" className="hp-signup-button-footer niveau-grotesk-black" clickMethod={props.navs.click.navSignup}/>
                </div>
          </div>
            <div className="hp-footer-menu-bar-mobile hp-border-bottom">
                <div className="hp-left-bar">  </div>
                <div className="hp-right-bar">
                    <HitParadeButton buttonText="Beta Sign Up" className="hp-signup-button-footer niveau-grotesk-black" clickMethod={props.navs.click.navSignup}/>
                </div>
            </div>
            <div className="hp-footer-menu-bar-mobile">

              <div className="hp-left-bar hp-privacy-statement">
                  <HitParadeLeftMenuItem imgRoot={props.imgRoot} menuItemText="Privacy Statement" classNames="hp-privacy-statement hp-footer-font-size hp-footer-item proxima-nova-regular" clickMethod={props.navs.click.navPrivacyStatement} />
              </div>
              <div className="hp-footer-font-size hp-right-bar hp-copyright proxima-nova-regular">
                  &copy; Hit Parade Inc {fullYear}
              </div>

          </div>
        </div>
      </div>
    </footer>
  );
};

HitParadeFooter.propTypes = {
  svgs: PropTypes.object.isRequired,
  playersInCart: PropTypes.number.isRequired,
};

export default HitParadeFooter;
