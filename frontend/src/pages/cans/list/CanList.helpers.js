import { USER_ROLES } from "../../../components/Users/User.constants";
/**
 * @typedef {import('./././CANFilterButton/CANFilterTypes').FilterOption} FilterOption
 * @typedef {import('./././CANFilterButton/CANFilterTypes').Filters} Filters
 */

/**
 * @description Sorts and filters the array of CANs.
 * @typedef {import("../../../components/CANs/CANTypes").CAN} CAN
 * @param {CAN[]} cans - The array of CANs to sort.
 * @param {boolean} myCANsUrl - The URL parameter to filter by "my-CANs".
 * @param {import("../../../components/Users/UserTypes").User} activeUser - The active user.
 * @param {Filters} filters - The filters to apply.
 * @returns {CAN[]} - The sorted array of CANs.
 */
export const sortAndFilterCANs = (cans, myCANsUrl, activeUser, filters) => {
    if (!cans || cans.length === 0) {
        return [];
    }

    const { roles, id: userId, division: userDivisionId } = activeUser;
    // NOTE: Role-based filtering
    let filteredCANs = cans.filter((can) => {
        // Always include CAN if the user is not filtering by "my-CANs"
        if (!myCANsUrl) return true;

        // Check if user has any role that allows access to all CANs
        if (roles.some((role) => [USER_ROLES.SYSTEM_OWNER].includes(role))) return true;

        // Filter based on specific roles division directors and budget team
        if (roles.includes(USER_ROLES.REVIEWER_APPROVER || USER_ROLES.BUDGET_TEAM)) {
            return can.portfolio.division_id === userDivisionId;
        }
        // Filter based on team members
        // TODO: add project officers per #2884
        if (roles.includes(USER_ROLES.USER)) {
            return can.budget_line_items.some((bli) => bli.team_members.some((member) => member.id === userId));
        }

        // If no specific role matches, don't include the CAN
        return false;
    });

    // NOTE: Filter by filter prop
    filteredCANs = applyAdditionalFilters(filteredCANs, filters);

    return sortCANs(filteredCANs);
};

/**
 * @description Sorts an array of CANs by obligateBy date in descending order.
 * @param {CAN[]} cans - The array of CANs to sort.
 * @returns {CAN[] | []} - The sorted array of CANs.
 */
const sortCANs = (cans) => {
    if (!cans) {
        return [];
    }

    return [...cans].sort((a, b) => {
        const dateA = a.obligate_by ? new Date(a.obligate_by).getTime() : 0;
        const dateB = b.obligate_by ? new Date(b.obligate_by).getTime() : 0;
        return dateB - dateA;
    });
};

/**
 * @description Applies additional filters to the CANs.
 * @param {CAN[]} cans - The array of CANs to filter.
 * @param {Filters} filters - The filters to apply.
 * @returns {CAN[]} - The filtered array of CANs.
 */
const applyAdditionalFilters = (cans, filters) => {
    let filteredCANs = cans;

    // Filter by active period
    if (filters.activePeriod && filters.activePeriod.length > 0) {
        filteredCANs = filteredCANs.filter((can) =>
            filters.activePeriod?.some((period) => period.id === can.active_period)
        );
    }

    if (filters.transfer && filters.transfer.length > 0) {
        filteredCANs = filteredCANs.filter((can) =>
            filters.transfer?.some(
                (transfer) => transfer.title.toUpperCase() === can.funding_details?.method_of_transfer
            )
        );
    }

    if (filters.portfolio && filters.portfolio.length > 0) {
        filteredCANs = filteredCANs.filter((can) =>
            filters.portfolio?.some(
                (portfolio) => portfolio.title == `${can.portfolio.name} (${can.portfolio.abbreviation})`
            )
        );
    }

    if (filters.budget && filters.budget.length > 0) {
        filteredCANs = filteredCANs.filter((can) => {
            // Skip CANs with no funding budgets or only null budgets
            const validBudgets = can.funding_budgets?.filter((b) => b.budget !== null);
            if (validBudgets?.length === 0) return false;

            // Check if any valid budget falls within range
            return validBudgets?.some(
                (budget) => budget.budget >= filters.budget[0] && budget.budget <= filters.budget[1]
            );
        });
    }

    // TODO: Add other filters here
    // Example:
    // if (filters.someOtherFilter && filters.someOtherFilter.length > 0) {
    //     filteredCANs = filteredCANs.filter((can) => {
    //         // Apply some other filter logic
    //     });
    // }

    return filteredCANs;
};

/**
 * @description Returns a set of unique portfolios from the CANs list
 * @param {CAN[]} cans - The array of CANs to filter.
 * @returns {FilterOption[]} - The filtered array of portfolios.
 */
export const getPortfolioOptions = (cans) => {
    if (!cans || cans.length === 0) {
        return [];
    }
    const portfolios = cans.reduce((acc, can) => {
        const { name, abbreviation } = can.portfolio;
        const uniqueKey = `${name}_${abbreviation}`;
        acc.add(uniqueKey);
        return acc;
    }, new Set());

    return Array.from(portfolios)
        .sort((a, b) => {
            const [nameA] = a.split("_");
            const [nameB] = b.split("_");
            return nameA.localeCompare(nameB);
        })
        .map((uniqueKey, index) => {
            const [name, abbr] = uniqueKey.split("_");
            return {
                id: index,
                title: `${name} (${abbr})`,
                abbr: abbr
            };
        });
};

export const getSortedFYBudgets = (cans) => {
    if (!cans || cans.length === 0) {
        return [];
    }

    const funding_budgets = cans.reduce((acc, can) => {
        acc.add(can.funding_budgets);
        return acc;
    }, new Set());

    return Array.from(funding_budgets)
        .flatMap((itemArray) => itemArray.map((item) => item.budget))
        .sort((a, b) => a - b);
};
