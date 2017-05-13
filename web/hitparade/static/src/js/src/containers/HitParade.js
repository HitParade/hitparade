import React, { Component, PropTypes } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import ReactModal from 'react-modal';

import * as HitParadeActionCreators from '../actions/hitparade';
import HitParadeHeader from '../components/HitParadeHeader';
import HitParadeFooter from '../components/HitParadeFooter';
import HitParadeHeroImage from '../components/HitParadeHeroImage';
import HitParadeSectionWhy from '../components/HitParadeSectionWhy';
import HitParadeHowItWorks from '../components/HitParadeHowItWorks';
import HitParadeMailChimp from '../components/HitParadeMailChimp';

class HitParade extends Component {
  static propTypes = {
      playersInCart: PropTypes.number.isRequired,
      heroImage: PropTypes.string.isRequired,
      heroImageMobile: PropTypes.string.isRequired,
      svgs: PropTypes.object.isRequired,
      showModal: PropTypes.bool.isRequired,
  };
  render() {
      const { dispatch, imgRoot, playersInCart, heroImage, heroImageMobile, svgs, showModal } = this.props;
      const selectPlayer = bindActionCreators(HitParadeActionCreators.selectPlayer, dispatch);
      const removePlayer = bindActionCreators(HitParadeActionCreators.removePlayer, dispatch);

      /**
      *   NAVIGATION
      */
      const closeModal = bindActionCreators(HitParadeActionCreators.closeModal, dispatch);
      const navLogin = bindActionCreators(HitParadeActionCreators.navLogin, dispatch);
      const navSignup = bindActionCreators(HitParadeActionCreators.navSignup, dispatch);
      const navContact = bindActionCreators(HitParadeActionCreators.navContact, dispatch);
      const navFaq = bindActionCreators(HitParadeActionCreators.navFaq, dispatch);
      const navSelectPlayers = bindActionCreators(HitParadeActionCreators.navSelectPlayers, dispatch);
      const navShare = bindActionCreators(HitParadeActionCreators.navShare, dispatch);
      const cart = bindActionCreators(HitParadeActionCreators.cart, dispatch);
      const navTermsOfUse = bindActionCreators(HitParadeActionCreators.navTermsOfUse, dispatch);
      const navPrivacyStatement = bindActionCreators(HitParadeActionCreators.navPrivacyStatement, dispatch);
      const navigationMethods = {
        'click' : {
          'navLogin': navLogin,
          'navSignup': navSignup,
          'navContact': navContact,
          'navFaq': navFaq,
          'navSelectPlayers':navSelectPlayers,
          'navShare': navShare,
          'cart': cart,
          'navTermsOfUse': navTermsOfUse,
          'navPrivacyStatement': navPrivacyStatement,
        }
      };
  		return (
  			<div>
  				<HitParadeHeader isLive='false' playersInCart={playersInCart} svgs={svgs} navs={navigationMethods} imgRoot={imgRoot} />
  				<HitParadeHeroImage img={heroImage} imgMobile={heroImageMobile} navs={navigationMethods}  imgRoot={imgRoot} />
          <HitParadeSectionWhy  navs={navigationMethods} imgRoot={imgRoot}  />
          <HitParadeHowItWorks  navs={navigationMethods}  imgRoot={imgRoot} />
          <HitParadeFooter playersInCart={playersInCart} svgs={svgs} navs={navigationMethods}  imgRoot={imgRoot} />
          <ReactModal
           isOpen={showModal}
           contentLabel="Minimal Modal Example" >
                    <HitParadeMailChimp closeModal={closeModal} subscribe={closeModal}  imgRoot={imgRoot} />
          </ReactModal>

  			</div>
  		)
  }
}
//,
const mapStateToProps = state => ({
   playersInCart: state.playersInCart,
   heroImage: state.heroImage,
   heroImageMobile: state.heroImageMobile,
   svgs: state.svgs,
   showModal: state.showModal,
   imgRoot: state.imgRoot,
});

export default connect(mapStateToProps)(HitParade);