from typing import Literal

from pydantic import BaseModel, Field


class FundamentalAnalysis(BaseModel):
    overall_investment_thesis: str
    investment_grade: Literal["A", "B", "C", "D"]
    confidence_score: float = Field(ge=0, le=1)
    key_strengths: list[str] = Field(min_length=3, max_length=3)
    key_concerns: list[str] = Field(min_length=3, max_length=3)
    recommendation: Literal["buy", "hold", "sell", "avoid"]


class MomentumAnalysis(BaseModel):
    overall_momentum: Literal["positive", "neutral", "negative"]
    momentum_strength: Literal["strong", "moderate", "weak"]
    key_momentum_drivers: list[str] = Field(min_length=2, max_length=3)
    momentum_risks: list[str] = Field(min_length=2, max_length=3)
    short_term_outlook: Literal["bullish", "neutral", "bearish"]
    momentum_score: float = Field(ge=0, le=10)


class SentimentAnalysis(BaseModel):
    sentiment_score: float = Field(ge=1, le=10)
    sentiment_direction: Literal["Positive", "Neutral", "Negative"]
    key_news_themes: list[str]
    recent_catalysts: list[str]
    market_outlook: str


class FinalRecommendation(BaseModel):
    action: Literal["BUY", "HOLD", "SELL"]
    confidence: float = Field(ge=0, le=1)
    rationale: str
    key_risks: list[str]
    key_opportunities: list[str]
    time_horizon: Literal["Short-term", "Medium-term", "Long-term"]


class AgentRequest(BaseModel):
    query: str
    limit: int = 3


class AgentResponse(BaseModel):
    query: str
    ticker: str
    fundamental_analysis: FundamentalAnalysis
    momentum_analysis: MomentumAnalysis
    sentiment_analysis: SentimentAnalysis
    final_recommendation: FinalRecommendation
