import React, { Component, PropTypes } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import ReactModal from 'react-modal';
import { scroller } from 'react-scroll';
import responsive from '../../responsive';
import * as HitParadeActionCreators from '../actions/hitparade';
import HitParadeHeader from '../components/HitParadeHeader';
import HitParadeHeroImage from '../components/HitParadeHeroImage';
import HitParadeSectionWhy from '../components/HitParadeSectionWhy';
import HitParadeHowItWorks from '../components/HitParadeHowItWorks';
import HitParadeFooter from '../components/HitParadeFooter';
import HitParadeMailChimp from '../components/HitParadeMailChimp';
import SocialMediaShare from '../components/SocialMediaShare';
import MobileDrawer from '../components/MobileDrawer';
import MobileDrawerContent from '../components/MobileDrawerContent';
import Modal from '../components/Modal';

const scrollTargets = {
  howItWorks: 'howItWorksStepsReactScrollName'
}

class HitParade extends Component {
  static propTypes = {
      playersInCart: PropTypes.number.isRequired,
      heroImage: PropTypes.string.isRequired,
      heroImageMobile: PropTypes.string.isRequired,
      svgs: PropTypes.object.isRequired,
      showModal: PropTypes.bool.isRequired,
  }; 

  scrollTo(scrollTargetName) {
      const target = scrollTargets[scrollTargetName];
      console.log('target', target);
      scroller.scrollTo(target, {
          duration: 700,
          delay: 0,
          smooth: "easeOutElastic",
          offset: -100,
          smooth: true,
      })
   }

   modalContent(closeModal, showModal) {
     //TODO move to its own component
     const { 
       modalData,
       imgRoot
      } = this.props;
     let element = null;

      const mailChimp = (
          <HitParadeMailChimp 
                      closeModal={closeModal} 
                      subscribe={closeModal}  
                      imgRoot={imgRoot} 
                     />
        )

      const socialMediaShare = (
            <SocialMediaShare
              closeModal={closeModal} 
              className="social-media-share-container-background-white"
            />
          )

     switch (modalData) {
       case 'signUp':
        element = mailChimp;
       break;

       case 'share':
          element = socialMediaShare;
       break;
       default:
          element = socialMediaShare;
     }

     return element;
   }

  render() {
      const { 
        dispatch, 
        imgRoot, 
        playersInCart, 
        heroImage, 
        heroImageMobile, 
        svgs, 
        showModal,
        modalData,
        showDrawer
      } = this.props;

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
      const toggleHamburger = bindActionCreators(HitParadeActionCreators.toggleHamburger, dispatch);
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
       const styles = {
            fontFamily: 'Menlo-Regular, Menlo, monospace',
            fontSize: 14,
            lineHeight: '10px',
            color: 'white',
            display: 'flex', alignItems: 'center',
            justifyContent: 'center',
            contentHeaderMenuLink: {
                textDecoration: 'none',
                color: 'white',
                padding: 8,
              },
              content: {
                padding: '16px',
              },
        };

  		return (
  		    <div className="hp-hero-parallax-overlay">
                        <HitParadeHeader 
                          isLive='false' 
                          playersInCart={playersInCart} 
                          svgs={svgs} 
                          navs={navigationMethods}
                          toggleHamburger={toggleHamburger}
                          showDrawer={showDrawer}
                          imgRoot={imgRoot} 
                        />
                            <HitParadeHeroImage
                                scrollTo={{
                                  howItWorks: () => this.scrollTo('howItWorks')
                                }}
                                img={heroImage}
                                imgMobile={heroImageMobile}
                                navs={navigationMethods}
                                imgRoot={imgRoot} 
                            />

                            <HitParadeSectionWhy
                              parallax={() => this.refs.parallax.scrollTo(2)}
                              refs={this.refs}
                              navs={navigationMethods}
                              imgRoot={imgRoot}
                            />

                            <HitParadeHowItWorks  
                              navs={navigationMethods}  
                            />
                             <HitParadeFooter 
                              playersInCart={playersInCart} 
                              svgs={svgs} 
                              navs={navigationMethods}  
                              imgRoot={imgRoot} 
                            />
                  <Modal
                    isOpen={showModal}
                    closeModal={closeModal}
                  >
                    {this.modalContent(closeModal, showModal)}
                  </Modal>

                    <MobileDrawer
                      isOpen={showDrawer}
                    >
                      <MobileDrawerContent/>
                    </MobileDrawer>


                </div> )
  }
}

const mapStateToProps = state => {
    return {
      playersInCart: state.hitParade.playersInCart,
      heroImage: state.hitParade.heroImage,
      heroImageMobile: state.hitParade.heroImageMobile,
      svgs: state.hitParade.svgs,
      showModal: state.hitParade.showModal,
      imgRoot: state.hitParade.imgRoot,
      showDrawer: state.hitParade.showDrawer,
    }
};


export default connect(mapStateToProps)(HitParade);