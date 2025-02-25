import RoundedBox from "../../RoundedBox";

/**
 * @typedef {Object} CardProps
 * @property {string} [title] - The title of the card.
 * @property {string} [dataCy] - The data-cy attribute to add to the card.
 * @property {Object} [style] - The style object to apply to the card.
 * @property {React.ReactNode} children - The children to render.
 */

/**
 * @component - A card component that wraps children in a rounded box
 * @param {CardProps} props - The props of the component
 * @returns {JSX.Element} - The rendered component
 */
const Card = ({ title, children, dataCy = "", ...rest }) => {
    return (
        <RoundedBox
            dataCy={dataCy}
            data-testid={dataCy}
            {...rest} // this is real trust 🧡
        >
            {title && <h3 className="margin-0 margin-bottom-3 font-12px text-base-dark text-normal">{title}</h3>}
            {children}
        </RoundedBox>
    );
};

export default Card;
