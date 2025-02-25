import { Link, useLocation } from "react-router-dom";
import styles from "../../../components/Portfolios/PortfolioTabsSection/PortfolioTabsSection.module.scss";
import TabsSection from "../../../components/UI/TabsSection";

/**
 * A header section of the Budget lines list page that contains the filters.
 * @component
 * @returns {JSX.Element} - The procurement shop select element.
 */
const CANTags = () => {
    const location = useLocation();
    const selected = `font-sans-2xs text-bold ${styles.listItemSelected}`;
    const notSelected = `font-sans-2xs text-bold ${styles.listItemNotSelected}`;

    const paths = [
        {
            name: "",
            label: "All CANs"
        }
    ];

    const links = paths.map((path) => {
        const queryString = `${path.name}`;

        return (
            <Link
                to={queryString}
                className={location.search === queryString ? selected : notSelected}
                key={queryString}
                data-cy={location.search === queryString ? "tab-selected" : "tab-not-selected"}
            >
                {path.label}
            </Link>
        );
    });

    return (
        <TabsSection
            links={links}
            label="CANs Tabs Section"
        />
    );
};

export default CANTags;
