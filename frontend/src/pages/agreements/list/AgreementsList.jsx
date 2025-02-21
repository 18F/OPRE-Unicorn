import _ from "lodash";
import { useState } from "react";
import { useSelector } from "react-redux";
import { useSearchParams } from "react-router-dom";
import App from "../../../App";
import { useGetAgreementsQuery } from "../../../api/opsAPI";
import AgreementsTable from "../../../components/Agreements/AgreementsTable";
import ChangeRequests from "../../../components/ChangeRequests";
import TablePageLayout from "../../../components/Layouts/TablePageLayout";
import { BLI_STATUS } from "../../../helpers/budgetLines.helpers";
import { draftBudgetLineStatuses, getCurrentFiscalYear } from "../../../helpers/utils";
import AgreementsFilterButton from "./AgreementsFilterButton/AgreementsFilterButton";
import AgreementsFilterTags from "./AgreementsFilterTags/AgreementsFilterTags";
import AgreementTabs from "./AgreementsTabs";
import sortAgreements from "./utils";

/**
 * @typedef {import('../../../components/Agreements/AgreementTypes').Agreement} Agreement
 */
/**
 * @component Page for the Agreements List.
 * @returns {JSX.Element} - The component JSX.
 */
const AgreementsList = () => {
    const [searchParams] = useSearchParams();
    const [filters, setFilters] = useState({
        portfolio: ["test"],
        fiscalYear: ["FY 2023", "FY 2024", "FY2025"],
        budgetLineStatus: {
            draft: true,
            planned: true,
            executing: true,
            obligated: true
        }
    });

    // TODO: Move logic to a custom hook './useAgreementsList.hooks.js'
    const {
        data: agreements,
        error: errorAgreement,
        isLoading: isLoadingAgreement
    } = useGetAgreementsQuery({ refetchOnMountOrArgChange: true });

    const activeUser = useSelector((state) => state.auth.activeUser);
    const myAgreementsUrl = searchParams.get("filter") === "my-agreements";
    const changeRequestUrl = searchParams.get("filter") === "change-requests";

    if (isLoadingAgreement) {
        return (
            <App>
                <h1>Loading...</h1>
            </App>
        );
    }
    if (errorAgreement) {
        return (
            <App>
                <h1>Oops, an error occurred</h1>
            </App>
        );
    }

    // FILTERS
    /** @param{Agreement[]} agreements */
    let filteredAgreements = _.cloneDeep(agreements);

    switch (filters.upcomingNeedByDate) {
        case "next-30-days":
            filteredAgreements = filteredAgreements.filter(
                /** @param{Agreement} agreement */
                (agreement) => {
                    return agreement.budget_line_items.some((bli) => {
                        return (
                            bli.date_needed &&
                            new Date(bli.date_needed) <= new Date(new Date().getTime() + 30 * 24 * 60 * 60 * 1000)
                        );
                    });
                }
            );
            break;
        case "current-fy":
            filteredAgreements = filteredAgreements.filter(
                /** @param{Agreement} agreement */
                (agreement) => {
                    return agreement.budget_line_items.some((bli) => {
                        const currentFY = Number(getCurrentFiscalYear(new Date()));
                        const bliFY = new Date(bli.date_needed).getFullYear();
                        return bli.date_needed && bliFY === currentFY;
                    });
                }
            );
            break;
        case "next-6-months":
            filteredAgreements = filteredAgreements.filter(
                /** @param{Agreement} agreement */
                (agreement) => {
                    const now = new Date();
                    const sixMonthsFromNow = new Date(now.setMonth(now.getMonth() + 6));
                    return agreement.budget_line_items.some((bli) => {
                        return bli.date_needed && new Date(bli.date_needed) <= sixMonthsFromNow;
                    });
                }
            );
            break;
        case "all-time":
            break;
    }

    // filter by projects
    filteredAgreements = filteredAgreements.filter(
        /** @param{Agreement} agreement */
        (agreement) => {
            return (
                filters.projects.length === 0 ||
                filters.projects.some((project) => {
                    return project.id === agreement.project_id;
                })
            );
        }
    );

    // filter by project officers
    filteredAgreements = filteredAgreements.filter(
        /** @param{Agreement} agreement */
        (agreement) => {
            return (
                filters.projectOfficers.length === 0 ||
                filters.projectOfficers.some((po) => {
                    return po.id === agreement.project_officer_id;
                })
            );
        }
    );

    // filter by types
    filteredAgreements = filteredAgreements.filter(
        /** @param{Agreement} agreement */
        (agreement) => {
            return (
                filters.types.length === 0 ||
                filters.types.some((agreementType) => {
                    return agreementType === agreement.agreement_type;
                })
            );
        }
    );

    // filter by procurement shops
    filteredAgreements = filteredAgreements.filter(
        /** @param{Agreement} agreement */
        (agreement) => {
            return (
                filters.procurementShops.length === 0 ||
                filters.procurementShops.some((procurementShop) => {
                    return procurementShop.id === agreement.awarding_entity_id;
                })
            );
        }
    );

    // filter by budget line status
    filteredAgreements = filteredAgreements.filter(
        /** @param{Agreement} agreement */
        (agreement) => {
            return (
                (filters.budgetLineStatus.draft === true && agreement.budget_line_items.length === 0) ||
                (filters.budgetLineStatus.draft === true &&
                    agreement.budget_line_items.some((bli) => {
                        return draftBudgetLineStatuses.includes(bli.status);
                    })) ||
                (filters.budgetLineStatus.planned === true &&
                    agreement.budget_line_items.some((bli) => {
                        return bli.status === BLI_STATUS.PLANNED;
                    })) ||
                (filters.budgetLineStatus.executing === true &&
                    agreement.budget_line_items.some((bli) => {
                        return bli.status === BLI_STATUS.EXECUTING;
                    })) ||
                (filters.budgetLineStatus.obligated === true &&
                    agreement.budget_line_items.some((bli) => {
                        return bli.status === BLI_STATUS.OBLIGATED;
                    }))
            );
        }
    );

    let sortedAgreements = [];
    if (myAgreementsUrl) {
        const myAgreements = filteredAgreements.filter(
            /** @param{Agreement} agreement */
            (agreement) => {
                return agreement.team_members?.some((teamMember) => {
                    return teamMember.id === activeUser.id || agreement.project_officer_id === activeUser.id;
                });
            }
        );
        sortedAgreements = sortAgreements(myAgreements);
    } else {
        // all-agreements
        sortedAgreements = sortAgreements(filteredAgreements);
    }

    let subtitle = "All Agreements";
    let details = "This is a list of all agreements across OPRE. Draft budget lines are not included in the Totals.";
    if (myAgreementsUrl) {
        subtitle = "My Agreements";
        details =
            "This is a list of agreements you are listed as a Team Member on.  Draft budget lines are not included in the Totals.";
    }
    if (changeRequestUrl) {
        subtitle = "For Review";
        details =
            "This is a list of changes within your Division that require your review and approval. This list could include requests for budget changes, status changes or actions taking place during the procurement process.";
    }

    return (
        <App breadCrumbName="Agreements">
            {!changeRequestUrl && (
                <TablePageLayout
                    title="Agreements"
                    subtitle={subtitle}
                    details={details}
                    buttonText="Add Agreement"
                    buttonLink="/agreements/create"
                    TabsSection={<AgreementTabs />}
                    FilterTags={
                        <AgreementsFilterTags
                            filters={filters}
                            setFilters={setFilters}
                        />
                    }
                    FilterButton={
                        <AgreementsFilterButton
                            filters={filters}
                            setFilters={setFilters}
                        />
                    }
                    TableSection={<AgreementsTable agreements={sortedAgreements} />}
                />
            )}
            {changeRequestUrl && (
                <TablePageLayout
                    title="Agreements"
                    subtitle={subtitle}
                    details={details}
                    buttonText="Add Agreement"
                    buttonLink="/agreements/create"
                    TabsSection={<AgreementTabs />}
                >
                    <ChangeRequests />
                </TablePageLayout>
            )}
        </App>
    );
};

export default AgreementsList;
