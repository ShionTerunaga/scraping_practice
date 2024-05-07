import { fetcher } from "@/model"
import useSWR from "swr"

export const useMainNews = () => {
    const { data, isLoading } = useSWR("http://localhost:8000", fetcher)

    return {
        data,
        isLoading,
    }
}
