import { AgencyInfo } from "./AgencyInfo";
import { Identifier } from "./Idnetifier";
import { NavFooter } from "./NavFooter";

export const Footer = () => {
    return (
        <footer className="usa-footer">
            <div className="grid-container usa-footer__return-to-top">
                <a href="#">Return to top</a>
            </div>
            <div className="usa-footer__primary-section">
                <NavFooter />
            </div>
            <div className="usa-footer__secondary-section">
                <AgencyInfo />
            </div>
            <Identifier />
        </footer>
    );
};
